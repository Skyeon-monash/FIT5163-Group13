import time
import sys
import os

import numpy as np
from PIL import ImageQt, Image
from PySide6 import *
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QPropertyAnimation, QThread, Signal, QTimer
from PySide6.QtGui import QMovie, QDesktopServices
from PySide6.QtWidgets import QFileDialog
from ui_main import *
import cv2
from connection import ServerThread


class MainWindow(QMainWindow):
    def __init__(self):

        # variable
        self.resImg = None
        self.editImg = None
        self.imageFilePath = None
        self.videoFilePath = None
        self.seconds = 0
        self.brightness = 0
        self.contrast = 1.0

        ############################## GUI settings ##############################
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()  # create your own UI object
        self.ui.setupUi(self)  # set all the attributes of object[self]

        # set window appearance
        self.setWindowFlags(Qt.FramelessWindowHint)  # remove window border
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set main background to transparent
        self.setWindowTitle('HIDE NOWHERE')  # set window title
        self.setWindowIcon(QtGui.QIcon(':/images/images/images/PyDracula.png'))  # set icon

        # connect function with widget:
        # method1:[widgetName].[event].connect(functionName)
        # method2:[widgetNmae].[event]=functionName
        self.ui.closeAppBtn.clicked.connect(self.buttonClick)
        self.ui.maximizeRestoreAppBtn.clicked.connect(self.buttonClick)
        self.ui.minimizeAppBtn.clicked.connect(self.buttonClick)
        self.ui.contentTopBg.mouseMoveEvent = self.moveWindow
        self.ui.schoolSignBtn.clicked.connect(self.slideLeftMenu)

        # 左侧菜单栏页面切换
        self.ui.msgBtn.clicked.connect(self.page_change)
        self.ui.fileBtn.clicked.connect(self.page_change)
        self.ui.videoBtn.clicked.connect(self.page_change)
        self.ui.settingBtn.clicked.connect(self.page_change)

        # 主页按钮页面切换
        self.ui.pushButton_7.clicked.connect(self.page_change)
        self.ui.pushButton_8.clicked.connect(self.page_change)
        self.ui.pushButton_14.clicked.connect(self.page_change)

        # 后台的连接线程
        self.server_thread = ServerThread()
        self.server_thread.start()

        # 连接信息页面
        self.server_thread.connection_prompt_signal.connect(self.print_connection_prompt)  # 连接提示
        self.server_thread.connection_info_signal.connect(self.update_connection_info)  # 连接信息

        # 消息接收功能页面
        self.server_thread.message_recv_signal.connect(self.append_msg_recv)  # 消息接收功能
        self.ui.fileOpenBtn.clicked.connect(self.open_msg_path_sys)  # 打开文件路径按钮
        self.ui.clearBtn.clicked.connect(self.clear_msg_recv)  # 清空接收区
        self.ui.msgSaveBtn.clicked.connect(self.save_msg_recv)  # 保存接收到的消息

        # 文件接收功能页面
        self.server_thread.file_recv_signal.connect(self.print_file_recv_prompt)
        self.ui.fileOpenBtn1.clicked.connect(self.open_file_path_sys)
        self.ui.clearBtn1.clicked.connect(self.clear_msg_recv)

        # 视频接收功能页面
        self.server_thread.img_received_signal.connect(self.update_image)

        self.show()

    def print_connection_prompt(self, text):
        self.ui.connectionPrompt.append(text)

    def update_connection_info(self, info):
        self.ui.ipAddress.setText(info[0])
        self.ui.portNum.setText(info[1])
        self.ui.protocol.setText('TLS')
        self.ui.connectionTime.setText(info[2])
        self.ui.connectionStatus.setStyleSheet("color: #90ee90;")
        self.ui.connectionStatus.setText('Connected')

    def append_msg_recv(self, message):
        self.ui.messageRecv.append(message)

    def clear_msg_recv(self):
        self.ui.messageRecv.clear()

    def open_msg_path_sys(self):
        folderPath = QFileDialog.getExistingDirectory(
            self,
            'Choose a Directory',
            os.getcwd(),  # 程序当前工作目录  # 只显示 .txt 文件
        )
        if folderPath:
            self.ui.msgSavePath.setText(folderPath)

    def save_msg_recv(self):
        # 获取 QTextEdit 内容并去除首尾空白
        text = self.ui.messageRecv.toPlainText().strip()

        # 1. 检查内容是否为空
        if not text:
            return

        # 2. 保存到指定的文件路径
        save_path = self.ui.msgSavePath.text().strip()
        file_name = self.ui.msgSaveName.text().strip()
        path = ""
        if save_path and file_name:
            path = os.path.join(save_path, file_name)
            os.makedirs(os.path.dirname(path), exist_ok=True)  # 自动创建目录（如果不存在）
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(text)
            print("保存成功", f"内容已成功保存到 {path}")
        except Exception as e:
            print("保存失败", f"保存过程中出现错误：{str(e)}")

    def print_file_recv_prompt(self, text):
        self.ui.fileRecvPrompt.append(text)

    def clear_file_recv_prompt(self):
        self.ui.fileRecvPrompt.clear()

    def open_file_path_sys(self):
        folderPath = QFileDialog.getExistingDirectory(
            self,
            'Choose a Directory',
            os.getcwd(),  # 程序当前工作目录  # 只显示 .txt 文件
        )
        if folderPath:
            self.ui.fileSavePath.setText(folderPath)
            self.server_thread.set_file_path_signal.emit(folderPath)

    def page_change(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == 'msgBtn':
            self.buttonRestyle(btnName)
            self.buttonClickedStyle(btn)
            self.ui.stackedWidget.setCurrentIndex(1)
        elif btnName == 'fileBtn':
            self.buttonRestyle(btnName)
            self.buttonClickedStyle(btn)
            self.ui.stackedWidget.setCurrentIndex(2)
        elif btnName == 'videoBtn':
            self.buttonRestyle(btnName)
            self.buttonClickedStyle(btn)
            self.ui.stackedWidget.setCurrentIndex(3)
        elif btnName == 'settingBtn':
            self.buttonRestyle(btnName)
            self.buttonClickedStyle(btn)
            self.ui.stackedWidget.setCurrentIndex(4)
        elif btnName == 'pushButton_7':
            self.ui.stackedWidget.setCurrentIndex(1)
        elif btnName == 'pushButton_14':
            self.ui.stackedWidget.setCurrentIndex(2)
        elif btnName == 'pushButton_8':
            self.ui.stackedWidget.setCurrentIndex(3)

    def update_image(self, img: QImage):
        self.ui.videoDisplay.setPixmap(QPixmap.fromImage(img))

    def buttonClick(self):

        # get wigdet name
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'closeAppBtn' or btnName == 'exitBtn':
            self.close()

        if btnName == 'maximizeRestoreAppBtn':
            # if window already maximized
            if self.isMaximized():
                self.ui.maximizeRestoreAppBtn.setIcon(QIcon(':/icons/images/icons/icon_maximize.png'))  # change icon
                self.showNormal()  # show normal size
            else:
                self.ui.maximizeRestoreAppBtn.setIcon(QIcon(':/icons/images/icons/icon_restore.png'))
                self.showMaximized()

        if btnName == 'minimizeAppBtn':
            self.showMinimized()

        if btnName == 'pushButton':
            if self.videoFilePath == None:
                pass
            else:
                QDesktopServices.openUrl(self.videoFilePath)

    def mousePressEvent(self, event):
        # Get the current position of the mouse
        # We will use this value to move the window
        self.clickPosition = event.globalPosition().toPoint()

    def moveWindow(self, e):
        # Move window only when window is normal size
        if self.isMaximized() == False:
            # if left mouse button is clicked (Only accept left mouse button clicks)
            if e.buttons() == Qt.LeftButton:
                # Move window
                self.move(self.pos() + e.globalPosition().toPoint() - self.clickPosition)
                self.clickPosition = e.globalPosition().toPoint()
                e.accept()

    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.leftMenuBg.width()

        if width == 60:
            newWidth = 180
        else:
            newWidth = 60

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")  # Animate minimumWidth
        self.animation.setDuration(500)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: rgb(40, 44, 52);
        """

    # restyle menu button except btnName
    def buttonRestyle(self, btnName):
        for button in self.ui.leftMenuBg.findChildren(QPushButton):
            if button.objectName() != btnName and button.objectName() != self.ui.schoolSignBtn.objectName():
                button.setStyleSheet(button.styleSheet().replace(self.MENU_SELECTED_STYLESHEET, ""))

    def buttonClickedStyle(self, btnObject):
        btnObject.setStyleSheet(btnObject.styleSheet() + self.MENU_SELECTED_STYLESHEET)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
