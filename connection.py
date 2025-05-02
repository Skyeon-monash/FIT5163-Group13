import os
import socket
import ssl
import threading
import time
from dataclasses import dataclass

from PySide6.QtCore import Signal, QThread

import struct
import numpy as np
import cv2
from PySide6.QtGui import QImage

HOST = '127.0.0.1'
# HOST = '0.0.0.0'
PORT = 12345
BUFFER_SIZE = 4096

class ServerThread(QThread):
    connection_prompt_signal = Signal(str)
    connection_info_signal = Signal(list)
    message_recv_signal = Signal(str)
    file_recv_signal = Signal(str)
    set_file_path_signal = Signal(str)
    img_received_signal = Signal(QImage)

    def __init__(self):
        super().__init__()
        self.file_save_path = None
        self.running = True
        self.set_file_path_signal.connect(self.set_file_save_path)

    def run(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((HOST, PORT))
            sock.listen(5)
            self.connection_prompt_signal.emit("服务器已启动，等待连接...")

            with context.wrap_socket(sock, server_side=True) as ssock:
                ssock.settimeout(1.0)  # 便于检查 self.running
                while self.running:
                    try:
                        conn, addr = ssock.accept()
                        ip, port = addr
                        connect_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        info = [ip, str(port), connect_time]
                        self.connection_info_signal.emit(info)
                        self.connection_prompt_signal.emit(f"已连接：{addr}")

                        client_thread = threading.Thread(
                            target=self.handle_client, args=(conn, addr), daemon=True
                        )
                        client_thread.start()
                    except socket.timeout:
                        continue
                    except Exception as e:
                        self.connection_prompt_signal.emit(f"连接处理异常: {str(e)}")

    def stop(self):
        self.running = False
        self.connection_prompt_signal.emit("服务器即将关闭...")

    def handle_client(self, conn, addr):
        while True:
            try:
                while True:
                    choice = conn.recv(BUFFER_SIZE).decode()
                    if not choice:
                        break  # 客户端关闭连接或断电

                    self.connection_prompt_signal.emit(f"收到客户端 {addr} 的选择: {choice}")

                    if choice == "1":
                        self.receive_message(conn)
                    elif choice == "2":
                        self.receive_file(conn)
                    elif choice == "3":
                        self.receive_video(conn)
                    elif choice == "4":
                        self.connection_prompt_signal.emit(f"客户端 {addr} 请求断开连接")
                        break  # 跳出循环关闭连接
            except Exception as e:
                self.connection_prompt_signal.emit(f"客户端 {addr} 处理错误: {str(e)}")
            # finally:
            #     self.disconnect(conn)

    def disconnect(self, conn):
        try:
            conn.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass
        finally:
            conn.close()
            print("连接已断开")

    def receive_message(self, conn):
        msg = conn.recv(BUFFER_SIZE).decode()
        current_hms = time.strftime("%H:%M:%S", time.localtime())
        self.message_recv_signal.emit(f"Client[{current_hms}]: {msg}")

    def set_file_save_path(self, path):
        self.file_save_path = path

    def receive_file(self, conn):
        current_hms = time.strftime("%H:%M:%S", time.localtime())
        self.file_recv_signal.emit(f"[{current_hms}]: 客户端开始传输文件...")
        if self.file_save_path:
            file_name = conn.recv(BUFFER_SIZE).decode()
            file_path = os.path.join(self.file_save_path, file_name)
            with open(file_path, 'wb') as f:
                while True:
                    data = conn.recv(BUFFER_SIZE)
                    if data == b'22222222':
                        break
                    f.write(data)
            current_hms = time.strftime("%H:%M:%S", time.localtime())
            self.file_recv_signal.emit(f"[{current_hms}]: 文件 {file_name} 接收完成")

    def receive_video(self, conn):
        try:
            while True:
                raw_len = self.recv_all(conn, 4)
                if not raw_len:
                    break
                msg_len = struct.unpack('!I', raw_len)[0]

                frame_data = self.recv_all(conn, msg_len)
                if not frame_data:
                    break

                img_np = np.frombuffer(frame_data, dtype=np.uint8)
                frame = cv2.imdecode(img_np, flags=1)

                if frame is not None:
                    # cv2.imshow('接收视频', frame)
                    h, w, ch = frame.shape
                    bytes_per_line = ch * w
                    qt_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_BGR888)
                    self.img_received_signal.emit(qt_img)
                    self.msleep(33)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
        except Exception as e:
            self.connection_prompt_signal.emit(f"视频接收错误: {str(e)}")
        finally:
            cv2.destroyAllWindows()

    def recv_all(self, sock, n):
        data = b''
        while len(data) < n:
            packet = sock.recv(n - len(data))
            if not packet:
                return None
            data += packet
        return data
