from flask import Flask, render_template, request, redirect, url_for  # 添加request导入
import os
app = Flask(__name__)

# 定义要显示的文件目录（根据实际情况修改）
FILE_DIRECTORY = "TransDoc"
BUFFER_SIZE = 65536  # 每次发送数据块大小
global_ssock = None

def Send_Message(ssock,NameMessage):
    try:
        ssock.send(NameMessage)
        # data = ssock.recv(BUFFER_SIZE)
        # print("成功收到响应:", data.decode())
        # break
    except Exception as e:
        print("消息发送失败")
def send_all(sock, data):
    bytes_sent = 0
    while bytes_sent < len(data):
        sent = sock.send(data[bytes_sent:])
        if sent == 0:
            raise RuntimeError("Socket连接断开")
        bytes_sent += sent
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 拼接IP地址
        ipadd = '.'.join([
            request.form.get('text1'),
            request.form.get('text2'),
            request.form.get('text3'),
            request.form.get('text4')
        ])
        print("登录IP地址:", ipadd)
        import socket
        import ssl
        import time
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

                # data = ssock.recv(BUFFER_SIZE)
                # ssock.send(b"Hello from TLS Client!")
                # data = ssock.recv(BUFFER_SIZE)
                # print("成功收到响应:", data.decode())
                # break
        global global_ssock
        HOST = ipadd
        PORT =12345
        sock = socket.create_connection((HOST, PORT), timeout=5)
        ssock =context.wrap_socket(sock, server_hostname=HOST)
        global_ssock = ssock

        # 重定向到主页（会触发GET请求）
        return redirect(url_for('home'))  # 关键修改点

    return render_template('login.html')
@app.route('/test', methods=['GET', 'POST'])
def home():
    global global_ssock
    if request.method == 'POST':
        # 获取被点击按钮的标识
        submit_action = request.form.get('submit_action')
        choice = 0
        if submit_action == 'text_submit':
            # 处理文本输入
            text_content = request.form.get('text_input')
            print("文本内容:", text_content)
            choice = '1'
            Send_Message(global_ssock, choice.encode())
            Send_Message(global_ssock, text_content.encode())

        elif submit_action == 'file_submit':
            # 获取下拉框选择的文件名
            selected_file = request.form.get('selected_file')
            if selected_file:
                print("选择的文件:", selected_file)
                # 这里可以添加文件处理逻辑（如读取内容、返回文件路径等）
            else:
                print("未选择文件")
            choice = '2'
            FILE_PATH = selected_file
            Send_Message(global_ssock, choice.encode())
            Send_Message(global_ssock, FILE_PATH.encode())
            # 读取并发送文件
            with open(FILE_DIRECTORY+'/'+FILE_PATH, 'rb') as f:
                while True:
                    data = f.read(BUFFER_SIZE)
                    
                    if not data:
                        break

                    global_ssock.send(data)
                global_ssock.send(b'22222222')
                print("[+] 文件接收完成")

        elif submit_action == 'video_submit':
            choice ='3'
            Send_Message(global_ssock, choice.encode())
            import cv2
            import struct
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

            try:
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break

                    # 压缩帧为JPEG格式 (调整质量参数)
                    _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
                    client_socket = global_ssock
                    # 发送帧长度和帧数据
                    data = buffer.tobytes()
                    msg_len = struct.pack('!I', len(data))  # 4字节网络字节序
                    send_all(client_socket, msg_len)
                    send_all(client_socket, data)

                    # 本地预览 (可选)
                    cv2.imshow('发送视频', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            finally:
                cap.release()
                client_socket.close()
                cv2.destroyAllWindows()

    # 获取文件列表（保持原有逻辑）
    try:
        files = [f for f in os.listdir(FILE_DIRECTORY)
                 if os.path.isfile(os.path.join(FILE_DIRECTORY, f))]
    except Exception as e:
        files = []
        print(f"Error reading directory: {e}")

    return render_template('index.html', file_list=files)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)