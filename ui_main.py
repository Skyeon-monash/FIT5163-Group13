# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainYOXKOS.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(946, 586)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"}")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.centralWidget)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"font{color:rgb(255,255,255)}")
        self.bgApp.setFrameShape(QFrame.Shape.StyledPanel)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.bgApp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(0, 16777215))
        self.leftMenuBg.setStyleSheet(u"#leftMenuBg {	\n"
"	background-color: #21252b;\n"
"}\n"
"\n"
"#topLogo {\n"
"	background-color: #21252b;\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"#titleLeftApp { font: 700 10pt \"Segoe UI Semibold\"; color:#ffffff;}\n"
"\n"
"#titleLeftDescription { font: 600 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"#leftMenuTop {	\n"
"	background-color: #21252b;\n"
"}\n"
"\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: #f8f8f2;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#topMenu {	\n"
"	background-color: #21252b;\n"
"}\n"
"\n"
""
                        "#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#bottomMenu {	\n"
"	background-color: #21252b;\n"
"}")
        self.leftMenuBg.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.leftMenuTop = QFrame(self.leftMenuBg)
        self.leftMenuTop.setObjectName(u"leftMenuTop")
        self.leftMenuTop.setMinimumSize(QSize(0, 60))
        self.leftMenuTop.setMaximumSize(QSize(16777215, 60))
        self.leftMenuTop.setStyleSheet(u"")
        self.leftMenuTop.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftMenuTop.setFrameShadow(QFrame.Shadow.Raised)
        self.schoolSignBtn = QPushButton(self.leftMenuTop)
        self.schoolSignBtn.setObjectName(u"schoolSignBtn")
        self.schoolSignBtn.setGeometry(QRect(9, 9, 40, 42))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.schoolSignBtn.sizePolicy().hasHeightForWidth())
        self.schoolSignBtn.setSizePolicy(sizePolicy1)
        self.schoolSignBtn.setMinimumSize(QSize(40, 0))
        self.schoolSignBtn.setMaximumSize(QSize(40, 16777215))
        self.schoolSignBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/images/images/images/PyDracula.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.schoolSignBtn.setIcon(icon)
        self.schoolSignBtn.setIconSize(QSize(40, 40))
        self.frame = QFrame(self.leftMenuTop)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 11, 111, 41))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.titleLeftApp = QLabel(self.frame)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\";")
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.titleLeftApp)

        self.titleLeftDescription = QLabel(self.frame)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setStyleSheet(u"font: 500 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.titleLeftDescription)


        self.verticalLayout_5.addWidget(self.leftMenuTop)

        self.topMenu = QFrame(self.leftMenuBg)
        self.topMenu.setObjectName(u"topMenu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.topMenu.sizePolicy().hasHeightForWidth())
        self.topMenu.setSizePolicy(sizePolicy2)
        self.topMenu.setStyleSheet(u"")
        self.topMenu.setFrameShape(QFrame.Shape.StyledPanel)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.topMenu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.msgBtn = QPushButton(self.topMenu)
        self.msgBtn.setObjectName(u"msgBtn")
        self.msgBtn.setMinimumSize(QSize(0, 45))
        self.msgBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.msgBtn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-closed.png);\n"
"font: 700 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"")

        self.verticalLayout_7.addWidget(self.msgBtn, 0, Qt.AlignmentFlag.AlignTop)

        self.fileBtn = QPushButton(self.topMenu)
        self.fileBtn.setObjectName(u"fileBtn")
        self.fileBtn.setMinimumSize(QSize(0, 45))
        self.fileBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fileBtn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);\n"
"font: 700 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.verticalLayout_7.addWidget(self.fileBtn)

        self.videoBtn = QPushButton(self.topMenu)
        self.videoBtn.setObjectName(u"videoBtn")
        self.videoBtn.setMinimumSize(QSize(0, 45))
        self.videoBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.videoBtn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-movie.png);\n"
"font: 700 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.verticalLayout_7.addWidget(self.videoBtn)


        self.verticalLayout_5.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuBg)
        self.bottomMenu.setObjectName(u"bottomMenu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bottomMenu.sizePolicy().hasHeightForWidth())
        self.bottomMenu.setSizePolicy(sizePolicy3)
        self.bottomMenu.setMinimumSize(QSize(0, 45))
        self.bottomMenu.setMaximumSize(QSize(16777215, 45))
        self.bottomMenu.setStyleSheet(u"")
        self.bottomMenu.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.settingBtn = QPushButton(self.bottomMenu)
        self.settingBtn.setObjectName(u"settingBtn")
        sizePolicy1.setHeightForWidth(self.settingBtn.sizePolicy().hasHeightForWidth())
        self.settingBtn.setSizePolicy(sizePolicy1)
        self.settingBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settingBtn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-settings.png);\n"
"font: 700 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"")

        self.verticalLayout_8.addWidget(self.settingBtn)


        self.verticalLayout_5.addWidget(self.bottomMenu)


        self.horizontalLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        sizePolicy3.setHeightForWidth(self.contentBox.sizePolicy().hasHeightForWidth())
        self.contentBox.setSizePolicy(sizePolicy3)
        self.contentBox.setMinimumSize(QSize(0, 0))
        self.contentBox.setMaximumSize(QSize(16777215, 16777215))
        self.contentBox.setStyleSheet(u"#bottomBar { background-color: #2c313a }\n"
"\n"
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"#contentTopBg{	\n"
"	background-color: #21252b;\n"
"}\n"
"\n"
"#titleRightInfo{\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"#subtitleRightInfo{\n"
"    color: #f8f8f2;\n"
"}")
        self.contentBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.contentTopBg.sizePolicy().hasHeightForWidth())
        self.contentTopBg.setSizePolicy(sizePolicy4)
        self.contentTopBg.setMinimumSize(QSize(0, 60))
        self.contentTopBg.setStyleSheet(u"")
        self.contentTopBg.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 6, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy4.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy4)
        self.leftBox.setStyleSheet(u"")
        self.leftBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.leftBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setStyleSheet(u"font: 700 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.verticalLayout_4.addWidget(self.titleRightInfo)

        self.subtitleRightInfo = QLabel(self.leftBox)
        self.subtitleRightInfo.setObjectName(u"subtitleRightInfo")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.subtitleRightInfo.setFont(font)
        self.subtitleRightInfo.setStyleSheet(u"font:  11pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.verticalLayout_4.addWidget(self.subtitleRightInfo)


        self.horizontalLayout_2.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setStyleSheet(u"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        self.rightButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.closeAppBtn)


        self.horizontalLayout_2.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg, 0, Qt.AlignmentFlag.AlignTop)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setStyleSheet(u"#contentBottom{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}")
        self.contentBottom.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        sizePolicy2.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy2)
        self.content.setFrameShape(QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.content)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"")
        self.pagesContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.pagesContainer)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(15, 15, 15, 15)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.horizontalLayout_14 = QHBoxLayout(self.home)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_20 = QFrame(self.home)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(350, 16777215))
        self.frame_20.setStyleSheet(u"")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_20)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy5)
        self.frame_24.setStyleSheet(u"#frame_24 {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 135, 135);\n"
"	font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_24)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 200))
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_25)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, 40, -1, -1)
        self.label_16 = QLabel(self.frame_25)
        self.label_16.setObjectName(u"label_16")
        sizePolicy5.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy5)
        self.label_16.setStyleSheet(u"font: 700 18pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_30.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_25)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_30.addWidget(self.label_17)


        self.verticalLayout_29.addWidget(self.frame_25, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_28.addWidget(self.frame_24)


        self.horizontalLayout_14.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.home)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 0))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_21)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(25, 70, -1, -1)
        self.frame_26 = QFrame(self.frame_21)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 100))
        self.frame_26.setStyleSheet(u"#frame_26 {\n"
"	border-radius: 10px;\n"
"	font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_26)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(10, 10, 10, 10)
        self.label_18 = QLabel(self.frame_26)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 700 18pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom-width:2 px;\n"
"border-bottom-color: rgb(189, 147, 249);\n"
"border-style:solid;")

        self.verticalLayout_32.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_26)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color:rgb(231, 231, 231);\n"
"font: 700 11pt \"Microsoft YaHei UI\";")

        self.verticalLayout_32.addWidget(self.label_19)


        self.verticalLayout_31.addWidget(self.frame_26, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_27 = QFrame(self.frame_21)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_27)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, 9, -1, -1)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(16777215, 30))
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_28)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_20 = QLabel(self.frame_28)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 700 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(230, 230, 230);")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_20)


        self.verticalLayout_33.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_29)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.pushButton_7 = QPushButton(self.frame_29)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 30))
        self.pushButton_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(106, 159, 159);\n"
"border-radius: 10px;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-envelope-closed.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon4)

        self.verticalLayout_35.addWidget(self.pushButton_7)

        self.pushButton_14 = QPushButton(self.frame_29)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 30))
        self.pushButton_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(106, 159, 159);\n"
"border-radius: 10px;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon5)

        self.verticalLayout_35.addWidget(self.pushButton_14)

        self.pushButton_8 = QPushButton(self.frame_29)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 30))
        self.pushButton_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(106, 159, 159);\n"
"border-radius: 10px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-movie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon6)

        self.verticalLayout_35.addWidget(self.pushButton_8)


        self.verticalLayout_33.addWidget(self.frame_29)


        self.verticalLayout_31.addWidget(self.frame_27)


        self.horizontalLayout_14.addWidget(self.frame_21)

        self.stackedWidget.addWidget(self.home)
        self.frame_21.raise_()
        self.frame_20.raise_()
        self.msgRecv = QWidget()
        self.msgRecv.setObjectName(u"msgRecv")
        self.verticalLayout_9 = QVBoxLayout(self.msgRecv)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(12, 12, 12, 12)
        self.frame_2 = QFrame(self.msgRecv)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 46))
        self.frame_2.setStyleSheet(u"#frame_2 QLabel{\n"
"	font:600 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:rgb(255,255,255);\n"
"}\n"
"\n"
"#frame_2 {\n"
"	border-bottom-width:2 px;\n"
"	border-bottom-color: rgb(189, 147, 249);\n"
"	border-style:solid;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"# label{\n"
"	font:600 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:rgb(255,255,255);\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.label)


        self.verticalLayout_9.addWidget(self.frame_2)

        self.imageDisplayFrame = QFrame(self.msgRecv)
        self.imageDisplayFrame.setObjectName(u"imageDisplayFrame")
        self.imageDisplayFrame.setMinimumSize(QSize(0, 300))
        self.imageDisplayFrame.setStyleSheet(u"#imageDisplayFrame QLabel {\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(52, 59, 72);\n"
"	font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}")
        self.imageDisplayFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.imageDisplayFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.imageDisplayFrame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.messageRecv = QTextEdit(self.imageDisplayFrame)
        self.messageRecv.setObjectName(u"messageRecv")
        self.messageRecv.setStyleSheet(u"    QTextEdit {\n"
"        background-color: rgb(27, 29, 35);\n"
"        border-radius: 5px;\n"
"        padding: 10px;\n"
"        selection-color: rgb(255, 255, 255);\n"
"        selection-background-color: rgb(255, 121, 198);\n"
"        color: white;\n"
"        font-size: 10pt;\n"
"        font-family: \"Segoe UI\", \"Microsoft YaHei UI\";\n"
"    }\n"
"    QTextEdit:hover {\n"
"        border: 2px solid rgb(64, 71, 88);\n"
"    }\n"
"    QTextEdit:focus {\n"
"        border: 2px solid rgb(91, 101, 124);\n"
"    }\n"
"\n"
"    QTextEdit QScrollBar:vertical {\n"
"        width: 8px;\n"
"    }\n"
"    QTextEdit QScrollBar:horizontal {\n"
"        height: 8px;\n"
"    }")
        self.messageRecv.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.messageRecv)


        self.verticalLayout_9.addWidget(self.imageDisplayFrame)

        self.chooseFileFrame = QFrame(self.msgRecv)
        self.chooseFileFrame.setObjectName(u"chooseFileFrame")
        self.chooseFileFrame.setMaximumSize(QSize(16777215, 60))
        self.chooseFileFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.chooseFileFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.chooseFileFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.msgSavePath = QLineEdit(self.chooseFileFrame)
        self.msgSavePath.setObjectName(u"msgSavePath")
        self.msgSavePath.setMinimumSize(QSize(0, 30))
        self.msgSavePath.setStyleSheet(u"color: rgb(217, 217, 217);")
        self.msgSavePath.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.msgSavePath)

        self.msgSaveName = QLineEdit(self.chooseFileFrame)
        self.msgSaveName.setObjectName(u"msgSaveName")
        self.msgSaveName.setMinimumSize(QSize(0, 30))
        self.msgSaveName.setStyleSheet(u"color: rgb(217, 217, 217);")
        self.msgSaveName.setReadOnly(False)

        self.horizontalLayout_9.addWidget(self.msgSaveName)

        self.fileOpenBtn = QPushButton(self.chooseFileFrame)
        self.fileOpenBtn.setObjectName(u"fileOpenBtn")
        self.fileOpenBtn.setMinimumSize(QSize(150, 30))
        self.fileOpenBtn.setStyleSheet(u"font: 700 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fileOpenBtn.setIcon(icon7)

        self.horizontalLayout_9.addWidget(self.fileOpenBtn)

        self.clearBtn = QPushButton(self.chooseFileFrame)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setMinimumSize(QSize(150, 30))
        self.clearBtn.setStyleSheet(u"font: 700 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-loop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearBtn.setIcon(icon8)

        self.horizontalLayout_9.addWidget(self.clearBtn)


        self.verticalLayout_9.addWidget(self.chooseFileFrame)

        self.imageSaveFrame = QFrame(self.msgRecv)
        self.imageSaveFrame.setObjectName(u"imageSaveFrame")
        self.imageSaveFrame.setMaximumSize(QSize(16777215, 25))
        self.imageSaveFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.imageSaveFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.imageSaveFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.msgSaveBtn = QPushButton(self.imageSaveFrame)
        self.msgSaveBtn.setObjectName(u"msgSaveBtn")
        sizePolicy1.setHeightForWidth(self.msgSaveBtn.sizePolicy().hasHeightForWidth())
        self.msgSaveBtn.setSizePolicy(sizePolicy1)
        self.msgSaveBtn.setStyleSheet(u"font: 700 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.msgSaveBtn.setIcon(icon9)

        self.verticalLayout_10.addWidget(self.msgSaveBtn)


        self.verticalLayout_9.addWidget(self.imageSaveFrame)

        self.stackedWidget.addWidget(self.msgRecv)
        self.fileRecv = QWidget()
        self.fileRecv.setObjectName(u"fileRecv")
        self.verticalLayout_91 = QVBoxLayout(self.fileRecv)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(12, 12, 12, 12)
        self.fileRecvTitle = QFrame(self.fileRecv)
        self.fileRecvTitle.setObjectName(u"fileRecvTitle")
        self.fileRecvTitle.setMaximumSize(QSize(16777215, 46))
        self.fileRecvTitle.setStyleSheet(u"#fileRecvTitle QLabel{\n"
"	font:600 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:rgb(255,255,255);\n"
"}\n"
"\n"
"#fileRecvTitle {\n"
"	border-bottom-width:2 px;\n"
"	border-bottom-color: rgb(189, 147, 249);\n"
"	border-style:solid;\n"
"}\n"
"")
        self.fileRecvTitle.setFrameShape(QFrame.Shape.StyledPanel)
        self.fileRecvTitle.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.fileRecvTitle)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.label1 = QLabel(self.fileRecvTitle)
        self.label1.setObjectName(u"label1")
        self.label1.setStyleSheet(u"# label{\n"
"	font:600 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:rgb(255,255,255);\n"
"}\n"
"")

        self.verticalLayout_131.addWidget(self.label1)


        self.verticalLayout_91.addWidget(self.fileRecvTitle)

        self.imageDisplayFrame1 = QFrame(self.fileRecv)
        self.imageDisplayFrame1.setObjectName(u"imageDisplayFrame1")
        self.imageDisplayFrame1.setMinimumSize(QSize(0, 300))
        self.imageDisplayFrame1.setStyleSheet(u"#imageDisplayFrame QLabel {\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(52, 59, 72);\n"
"	font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}")
        self.imageDisplayFrame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.imageDisplayFrame1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.imageDisplayFrame1)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.fileRecvPrompt = QTextEdit(self.imageDisplayFrame1)
        self.fileRecvPrompt.setObjectName(u"fileRecvPrompt")
        self.fileRecvPrompt.setStyleSheet(u"    QTextEdit {\n"
"        background-color: rgb(27, 29, 35);\n"
"        border-radius: 5px;\n"
"        padding: 10px;\n"
"        selection-color: rgb(255, 255, 255);\n"
"        selection-background-color: rgb(255, 121, 198);\n"
"        color: white;\n"
"        font-size: 10pt;\n"
"        font-family: \"Segoe UI\", \"Microsoft YaHei UI\";\n"
"    }\n"
"    QTextEdit:hover {\n"
"        border: 2px solid rgb(64, 71, 88);\n"
"    }\n"
"    QTextEdit:focus {\n"
"        border: 2px solid rgb(91, 101, 124);\n"
"    }\n"
"\n"
"    QTextEdit QScrollBar:vertical {\n"
"        width: 8px;\n"
"    }\n"
"    QTextEdit QScrollBar:horizontal {\n"
"        height: 8px;\n"
"    }")
        self.fileRecvPrompt.setReadOnly(True)

        self.verticalLayout_111.addWidget(self.fileRecvPrompt)


        self.verticalLayout_91.addWidget(self.imageDisplayFrame1)

        self.chooseFileFrame1 = QFrame(self.fileRecv)
        self.chooseFileFrame1.setObjectName(u"chooseFileFrame1")
        self.chooseFileFrame1.setMaximumSize(QSize(16777215, 60))
        self.chooseFileFrame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.chooseFileFrame1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.chooseFileFrame1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.fileSavePath = QLineEdit(self.chooseFileFrame1)
        self.fileSavePath.setObjectName(u"fileSavePath")
        self.fileSavePath.setMinimumSize(QSize(0, 30))
        self.fileSavePath.setStyleSheet(u"color: rgb(217, 217, 217);")
        self.fileSavePath.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.fileSavePath)

        self.fileOpenBtn1 = QPushButton(self.chooseFileFrame1)
        self.fileOpenBtn1.setObjectName(u"fileOpenBtn1")
        self.fileOpenBtn1.setMinimumSize(QSize(150, 30))
        self.fileOpenBtn1.setStyleSheet(u"font: 700 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);")
        self.fileOpenBtn1.setIcon(icon7)

        self.horizontalLayout_7.addWidget(self.fileOpenBtn1)

        self.clearBtn1 = QPushButton(self.chooseFileFrame1)
        self.clearBtn1.setObjectName(u"clearBtn1")
        self.clearBtn1.setMinimumSize(QSize(150, 30))
        self.clearBtn1.setStyleSheet(u"font: 700 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);")
        self.clearBtn1.setIcon(icon8)

        self.horizontalLayout_7.addWidget(self.clearBtn1)


        self.verticalLayout_91.addWidget(self.chooseFileFrame1)

        self.fileSaveFrame = QFrame(self.fileRecv)
        self.fileSaveFrame.setObjectName(u"fileSaveFrame")
        self.fileSaveFrame.setMaximumSize(QSize(16777215, 25))
        self.fileSaveFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.fileSaveFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.fileSaveFrame)
        self.verticalLayout_101.setSpacing(0)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_91.addWidget(self.fileSaveFrame)

        self.stackedWidget.addWidget(self.fileRecv)
        self.videoRecv = QWidget()
        self.videoRecv.setObjectName(u"videoRecv")
        self.videoRecv.setStyleSheet(u"QProgressBar{\n"
"	height:22px;\n"
"	text-align:center;\n"
"	font-size:14px; \n"
"	color:white; \n"
"	border-radius:11px; \n"
"	background:#1D5573;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:11px;\n"
"	background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #99ffff,stop:1 #9900ff);\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.videoRecv)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.vpTitle = QFrame(self.videoRecv)
        self.vpTitle.setObjectName(u"vpTitle")
        self.vpTitle.setMaximumSize(QSize(16777215, 46))
        self.vpTitle.setStyleSheet(u"#vpTitle QLabel{\n"
"	font:600 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:rgb(255,255,255);\n"
"}\n"
"\n"
"#vpTitle {\n"
"	border-bottom-width:2 px;\n"
"	border-bottom-color: rgb(189, 147, 249);\n"
"	border-style:solid;\n"
"}\n"
"")
        self.vpTitle.setFrameShape(QFrame.Shape.StyledPanel)
        self.vpTitle.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.vpTitle)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_2 = QLabel(self.vpTitle)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_15.addWidget(self.label_2)


        self.verticalLayout_14.addWidget(self.vpTitle)

        self.frame_4 = QFrame(self.videoRecv)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 250))
        self.frame_4.setStyleSheet(u"#frame_4 QLabel {\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(52, 59, 72);\n"
"	font: 700 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setMinimumSize(QSize(400, 0))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.videoDisplay = QLabel(self.frame_7)
        self.videoDisplay.setObjectName(u"videoDisplay")
        sizePolicy5.setHeightForWidth(self.videoDisplay.sizePolicy().hasHeightForWidth())
        self.videoDisplay.setSizePolicy(sizePolicy5)
        self.videoDisplay.setScaledContents(False)
        self.videoDisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.videoDisplay)


        self.verticalLayout_16.addWidget(self.frame_7)


        self.horizontalLayout_8.addWidget(self.frame_3)


        self.verticalLayout_14.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.videoRecv)
        self.deviceConnection = QWidget()
        self.deviceConnection.setObjectName(u"deviceConnection")
        self.verticalLayout_37 = QVBoxLayout(self.deviceConnection)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(12, 12, 12, 0)
        self.frame_33 = QFrame(self.deviceConnection)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(16777215, 46))
        self.frame_33.setStyleSheet(u"#frame_33 QLabel{\n"
"	font:600 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:rgb(255,255,255);\n"
"}\n"
"\n"
"#frame_33 {\n"
"	border-bottom-width:2 px;\n"
"	border-bottom-color: rgb(189, 147, 249);\n"
"	border-style:solid;\n"
"}\n"
"")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_33)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_21 = QLabel(self.frame_33)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_38.addWidget(self.label_21)


        self.verticalLayout_37.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.deviceConnection)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_34)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_46 = QFrame(self.frame_34)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(400, 0))
        self.frame_46.setMaximumSize(QSize(400, 16777215))
        self.frame_46.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(33, 37, 43);\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 121, 198);\n"
"	color: #ffb6c1; /* \u6de1\u7c89\u8272 */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    bord"
                        "er: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.frame_46.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_46)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(0, 50))
        self.frame_47.setMaximumSize(QSize(16777215, 50))
        self.frame_47.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.label_27 = QLabel(self.frame_47)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(90, 0))
        self.label_27.setMaximumSize(QSize(90, 16777215))
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_27)

        self.ipAddress = QLineEdit(self.frame_47)
        self.ipAddress.setObjectName(u"ipAddress")
        self.ipAddress.setMinimumSize(QSize(0, 30))
        self.ipAddress.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.ipAddress)


        self.verticalLayout_39.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.frame_46)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 50))
        self.frame_48.setMaximumSize(QSize(16777215, 50))
        self.frame_48.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, 0, -1, 0)
        self.label_28 = QLabel(self.frame_48)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(90, 0))
        self.label_28.setMaximumSize(QSize(90, 16777215))
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_28)

        self.portNum = QLineEdit(self.frame_48)
        self.portNum.setObjectName(u"portNum")
        self.portNum.setMinimumSize(QSize(0, 30))
        self.portNum.setReadOnly(True)

        self.horizontalLayout_27.addWidget(self.portNum)


        self.verticalLayout_39.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.frame_46)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(0, 50))
        self.frame_49.setMaximumSize(QSize(16777215, 50))
        self.frame_49.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 0, -1, 0)
        self.label_30 = QLabel(self.frame_49)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(90, 0))
        self.label_30.setMaximumSize(QSize(90, 16777215))
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_30)

        self.protocol = QLineEdit(self.frame_49)
        self.protocol.setObjectName(u"protocol")
        self.protocol.setMinimumSize(QSize(0, 30))
        self.protocol.setReadOnly(True)

        self.horizontalLayout_29.addWidget(self.protocol)


        self.verticalLayout_39.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_46)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 50))
        self.frame_50.setMaximumSize(QSize(16777215, 50))
        self.frame_50.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 0, -1, 0)
        self.label_31 = QLabel(self.frame_50)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(90, 0))
        self.label_31.setMaximumSize(QSize(90, 16777215))
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_31)

        self.connectionTime = QLineEdit(self.frame_50)
        self.connectionTime.setObjectName(u"connectionTime")
        self.connectionTime.setMinimumSize(QSize(0, 30))
        self.connectionTime.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.connectionTime)


        self.verticalLayout_39.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frame_46)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 50))
        self.frame_51.setMaximumSize(QSize(16777215, 50))
        self.frame_51.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, 0, -1, 0)
        self.label_32 = QLabel(self.frame_51)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(90, 0))
        self.label_32.setMaximumSize(QSize(90, 16777215))
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_32)

        self.connectionStatus = QLineEdit(self.frame_51)
        self.connectionStatus.setObjectName(u"connectionStatus")
        self.connectionStatus.setMinimumSize(QSize(0, 30))
        self.connectionStatus.setReadOnly(True)

        self.horizontalLayout_31.addWidget(self.connectionStatus)


        self.verticalLayout_39.addWidget(self.frame_51)


        self.verticalLayout_41.addWidget(self.frame_46, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_37.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.deviceConnection)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(16777215, 150))
        self.frame_35.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	b"
                        "order-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
" "
                        "   min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"#frame_35 {\n"
"	border-top-width:2 px;\n"
"	border-top-color: rgb(0, 170, 255);\n"
"	border-style:solid;\n"
"}")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, -1, -1, 0)
        self.connectionPrompt = QTextEdit(self.frame_37)
        self.connectionPrompt.setObjectName(u"connectionPrompt")
        self.connectionPrompt.setStyleSheet(u"    QTextEdit {\n"
"        background-color: rgb(27, 29, 35);\n"
"        border-radius: 5px;\n"
"        padding: 10px;\n"
"        selection-color: rgb(255, 255, 255);\n"
"        selection-background-color: rgb(255, 121, 198);\n"
"        color: white;\n"
"        font-size: 10pt;\n"
"        font-family: \"Segoe UI\", \"Microsoft YaHei UI\";\n"
"    }\n"
"    QTextEdit:hover {\n"
"        border: 2px solid rgb(64, 71, 88);\n"
"    }\n"
"    QTextEdit:focus {\n"
"        border: 2px solid rgb(91, 101, 124);\n"
"    }\n"
"\n"
"    QTextEdit QScrollBar:vertical {\n"
"        width: 8px;\n"
"    }\n"
"    QTextEdit QScrollBar:horizontal {\n"
"        height: 8px;\n"
"    }")
        self.connectionPrompt.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.connectionPrompt)


        self.horizontalLayout_17.addWidget(self.frame_37)


        self.verticalLayout_37.addWidget(self.frame_35)

        self.stackedWidget.addWidget(self.deviceConnection)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.pagesContainer)


        self.verticalLayout_3.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setStyleSheet(u"")
        self.bottomBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMinimumSize(QSize(0, 22))
        self.creditsLabel.setMaximumSize(QSize(16777215, 22))
        self.creditsLabel.setStyleSheet(u"font: 700 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.horizontalLayout_4.addWidget(self.creditsLabel, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.horizontalLayout.addWidget(self.contentBox)


        self.verticalLayout.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.schoolSignBtn.setText("")
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Course Design", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Group13", None))
        self.msgBtn.setText(QCoreApplication.translate("MainWindow", u"Msg Trans", None))
        self.fileBtn.setText(QCoreApplication.translate("MainWindow", u"File Trans", None))
        self.videoBtn.setText(QCoreApplication.translate("MainWindow", u"Real-time Video", None))
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"IoT Communication Server", None))
        self.subtitleRightInfo.setText(QCoreApplication.translate("MainWindow", u"An APP for interacting with IoT devices", None))
        self.minimizeAppBtn.setText("")
        self.maximizeRestoreAppBtn.setText("")
        self.closeAppBtn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Secure Communication", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TLS Encryption Support", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Two-way device verification & Lightweight deployment", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Choose one to start", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Message Transmission", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"File Transmission", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Real-time Video", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Message Transmission", None))
        self.messageRecv.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI','Microsoft YaHei UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.msgSavePath.setText(QCoreApplication.translate("MainWindow", u"Save Path", None))
        self.msgSavePath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6d88\u606f\u4fdd\u5b58\u8def\u5f84", None))
        self.msgSaveName.setText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.msgSaveName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None))
        self.fileOpenBtn.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.msgSaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"File Transmission", None))
        self.fileRecvPrompt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI','Microsoft YaHei UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.fileSavePath.setText(QCoreApplication.translate("MainWindow", u"Save Path", None))
        self.fileSavePath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u4fdd\u5b58\u8def\u5f84", None))
        self.fileOpenBtn1.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.clearBtn1.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Real-time Video", None))
        self.videoDisplay.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Device Connection", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"IP Address\uff1a", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Protocol:", None))
        self.protocol.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.connectionPrompt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI','Microsoft YaHei UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Presented by  Group 13", None))
    # retranslateUi

