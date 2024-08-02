# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AllPages.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/icon/Static/icon1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	\n"
"	border-image: url(:/img/Static/colorkit3.png);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.pageMain = QWidget()
        self.pageMain.setObjectName(u"pageMain")
        self.pageMain.setStyleSheet(u"\n"
"QPushButton {	\n"
"	color: #fff;\n"
"	border-radius: 5px;\n"
"	padding: 2px;\n"
"	background-color: #476f95;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"	background-color: #43698a;	\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.pageMain)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Widget1 = QWidget(self.pageMain)
        self.Widget1.setObjectName(u"Widget1")
        self.Widget1.setEnabled(True)
        self.Widget1.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.Widget1)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(1, 1, -1, 1)
        self.horizontalSpacer_3 = QSpacerItem(340, 424, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.widget_2 = QWidget(self.Widget1)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.button1exit = QPushButton(self.widget_2)
        self.button1exit.setObjectName(u"button1exit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button1exit.sizePolicy().hasHeightForWidth())
        self.button1exit.setSizePolicy(sizePolicy)
        self.button1exit.setMinimumSize(QSize(70, 30))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        self.button1exit.setFont(font)
        self.button1exit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.button1exit)


        self.gridLayout_3.addWidget(self.widget_2, 0, 2, 1, 1)

        self.frame = QFrame(self.Widget1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: #476f95;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"	background-color: #43698a;\n"
"	border-bottom: 1px solid #ffffff;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 50, 0, 100)
        self.button1add = QPushButton(self.frame)
        self.button1add.setObjectName(u"button1add")
        sizePolicy.setHeightForWidth(self.button1add.sizePolicy().hasHeightForWidth())
        self.button1add.setSizePolicy(sizePolicy)
        self.button1add.setMinimumSize(QSize(170, 0))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.button1add.setFont(font1)
        self.button1add.setToolTipDuration(-1)

        self.verticalLayout_4.addWidget(self.button1add)

        self.button1edit = QPushButton(self.frame)
        self.button1edit.setObjectName(u"button1edit")
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setPointSize(15)
        self.button1edit.setFont(font2)
        self.button1edit.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_4.addWidget(self.button1edit)

        self.button1status = QPushButton(self.frame)
        self.button1status.setObjectName(u"button1status")
        self.button1status.setFont(font2)
        self.button1status.setLayoutDirection(Qt.LeftToRight)
        self.button1status.setAutoFillBackground(False)

        self.verticalLayout_4.addWidget(self.button1status)

        self.button1learn = QPushButton(self.frame)
        self.button1learn.setObjectName(u"button1learn")
        self.button1learn.setFont(font2)
        self.button1learn.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_4.addWidget(self.button1learn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.Widget1)

        self.stackedWidget.addWidget(self.pageMain)
        self.pageAdd = QWidget()
        self.pageAdd.setObjectName(u"pageAdd")
        self.pageAdd.setStyleSheet(u"\n"
"\n"
"QPushButton {	\n"
"	color: #fff;\n"
"	border-radius: 5px;\n"
"	padding: 2px;\n"
"	background-color: #476f95;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"	background-color: #43698a;	\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.pageAdd)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Widget2 = QWidget(self.pageAdd)
        self.Widget2.setObjectName(u"Widget2")
        self.Widget2.setEnabled(True)
        self.gridLayout_4 = QGridLayout(self.Widget2)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(1, 1, -1, 1)
        self.frame_2 = QFrame(self.Widget2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: #476f95;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"	background-color: #43698a;\n"
"	border-bottom: 1px solid #ffffff;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 300, 0, 50)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.button2back = QPushButton(self.frame_2)
        self.button2back.setObjectName(u"button2back")
        sizePolicy.setHeightForWidth(self.button2back.sizePolicy().hasHeightForWidth())
        self.button2back.setSizePolicy(sizePolicy)
        self.button2back.setMinimumSize(QSize(170, 0))
        self.button2back.setFont(font1)
        self.button2back.setToolTipDuration(-1)

        self.verticalLayout_5.addWidget(self.button2back)


        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.Widget2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(117, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(49, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 1, 0, 2, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 186, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_5, 3, 1, 1, 1)

        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 45, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.button2addword = QPushButton(self.widget)
        self.button2addword.setObjectName(u"button2addword")
        self.button2addword.setMinimumSize(QSize(90, 30))
        self.button2addword.setFont(font)

        self.gridLayout_2.addWidget(self.button2addword, 0, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_2, 3, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(5)
        self.lineEdit2addEnglish = QLineEdit(self.widget)
        self.lineEdit2addEnglish.setObjectName(u"lineEdit2addEnglish")
        self.lineEdit2addEnglish.setMinimumSize(QSize(180, 30))
        self.lineEdit2addEnglish.setFont(font)
        self.lineEdit2addEnglish.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_8.addWidget(self.lineEdit2addEnglish, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.lineEdit2addRussian = QLineEdit(self.widget)
        self.lineEdit2addRussian.setObjectName(u"lineEdit2addRussian")
        self.lineEdit2addRussian.setMinimumSize(QSize(180, 30))
        self.lineEdit2addRussian.setFont(font)
        self.lineEdit2addRussian.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_8.addWidget(self.lineEdit2addRussian, 0, 2, 1, 1)

        self.frame_13 = QFrame(self.widget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(41, 41))
        self.frame_13.setMaximumSize(QSize(41, 41))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_13)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label2green_mark = QLabel(self.frame_13)
        self.label2green_mark.setObjectName(u"label2green_mark")
        self.label2green_mark.setMinimumSize(QSize(40, 40))
        self.label2green_mark.setMaximumSize(QSize(40, 40))
        self.label2green_mark.setStyleSheet(u"image: url(:/icon/Static/icons3.png);\n"
"")

        self.gridLayout_9.addWidget(self.label2green_mark, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_13, 0, 3, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.label2message = QLabel(self.widget)
        self.label2message.setObjectName(u"label2message")
        self.label2message.setMinimumSize(QSize(0, 0))
        self.label2message.setStyleSheet(u"color: #FF0000")

        self.gridLayout_7.addWidget(self.label2message, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_7, 0, 0, 1, 2)


        self.gridLayout_6.addWidget(self.widget, 1, 1, 2, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 187, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 0, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.Widget2)

        self.stackedWidget.addWidget(self.pageAdd)
        self.pageEdit = QWidget()
        self.pageEdit.setObjectName(u"pageEdit")
        self.pageEdit.setMinimumSize(QSize(250, 300))
        self.pageEdit.setStyleSheet(u"QPushButton {	\n"
"	color: #fff;\n"
"	border-radius: 5px;\n"
"	padding: 2px;\n"
"	background-color: #476f95;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"	background-color: #43698a;	\n"
"}")
        self.gridLayout_11 = QGridLayout(self.pageEdit)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Widget3 = QWidget(self.pageEdit)
        self.Widget3.setObjectName(u"Widget3")
        self.Widget3.setEnabled(True)
        self.gridLayout_12 = QGridLayout(self.Widget3)
        self.gridLayout_12.setSpacing(6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(1, 1, -1, 1)
        self.widget_3 = QWidget(self.Widget3)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setVerticalSpacing(12)
        self.gridLayout_13.setContentsMargins(-1, 25, -1, -1)
        self.button3delete = QPushButton(self.widget_3)
        self.button3delete.setObjectName(u"button3delete")
        self.button3delete.setMinimumSize(QSize(80, 30))
        self.button3delete.setFont(font)

        self.gridLayout_13.addWidget(self.button3delete, 0, 0, 1, 1)

        self.button3change = QPushButton(self.widget_3)
        self.button3change.setObjectName(u"button3change")
        self.button3change.setMinimumSize(QSize(80, 30))
        self.button3change.setFont(font)

        self.gridLayout_13.addWidget(self.button3change, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_13)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)


        self.gridLayout_12.addWidget(self.widget_3, 0, 4, 1, 1)

        self.frame_4 = QFrame(self.Widget3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 0))
        self.frame_4.setMaximumSize(QSize(200, 16777215))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"	background-color: #476f95;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"	\n"
"	border-bottom: 1px solid #ffffff;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 50, 0, 50)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 55))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame {	\n"
"	border-radius: 5px;\n"
"	background-color: #d1dbe4;\n"
"\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_6)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(0)
        self.lineEdit3find = QLineEdit(self.frame_6)
        self.lineEdit3find.setObjectName(u"lineEdit3find")
        self.lineEdit3find.setFont(font)
        self.lineEdit3find.setStyleSheet(u"QLineEdit {\n"
"	background-color: #d1dbe4\n"
"}")
        self.lineEdit3find.setFrame(False)

        self.gridLayout_16.addWidget(self.lineEdit3find, 0, 2, 1, 1)

        self.widget_4 = QWidget(self.frame_6)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(25, 25))
        self.widget_4.setStyleSheet(u"")
        self.gridLayout_17 = QGridLayout(self.widget_4)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(3, 3, 3, 3)
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(25, 25))
        self.label_4.setStyleSheet(u"image: url(:/icon/Static/icons8-\u043f\u043e\u0438\u0441\u043a-50.png);")

        self.gridLayout_17.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_4, 0, 1, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_16, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_6, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QLineEdit {	\n"
"	border-radius: 5px;\n"
"	border: 1px solid #d1dbe4;\n"
"	padding: 5px;\n"
"	background-color: #d1dbe4;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(16)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit3reEnglish = QLineEdit(self.frame_7)
        self.lineEdit3reEnglish.setObjectName(u"lineEdit3reEnglish")
        self.lineEdit3reEnglish.setFont(font)
        self.lineEdit3reEnglish.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.lineEdit3reEnglish)

        self.lineEdit3reRussian = QLineEdit(self.frame_7)
        self.lineEdit3reRussian.setObjectName(u"lineEdit3reRussian")
        self.lineEdit3reRussian.setFont(font)
        self.lineEdit3reRussian.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.lineEdit3reRussian)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_8)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(6)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(-1, -1, 0, -1)
        self.button3save = QPushButton(self.frame_8)
        self.button3save.setObjectName(u"button3save")
        self.button3save.setMinimumSize(QSize(0, 30))
        self.button3save.setFont(font)

        self.gridLayout_19.addWidget(self.button3save, 0, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_19, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_8)

        self.button3back = QPushButton(self.frame_4)
        self.button3back.setObjectName(u"button3back")
        self.button3back.setFont(font2)
        self.button3back.setLayoutDirection(Qt.LeftToRight)
        self.button3back.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.button3back)


        self.gridLayout_12.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_9 = QFrame(self.Widget3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_9)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(25, 25, 0, 50)
        self.listWidget3_showdata = QListWidget(self.frame_9)
        self.listWidget3_showdata.setObjectName(u"listWidget3_showdata")
        self.listWidget3_showdata.setMinimumSize(QSize(250, 0))
        font3 = QFont()
        font3.setPointSize(10)
        self.listWidget3_showdata.setFont(font3)
        self.listWidget3_showdata.setStyleSheet(u"QListWidget {\n"
"	padding: 5px;\n"
"	background-color: #fff;\n"
"	border: 1px solid #194a7a;\n"
"	border-radius: 4px;\n"
"}\n"
"")

        self.gridLayout_20.addWidget(self.listWidget3_showdata, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_9, 0, 3, 1, 1)


        self.gridLayout_11.addWidget(self.Widget3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageEdit)
        self.pageStatus = QWidget()
        self.pageStatus.setObjectName(u"pageStatus")
        self.pageStatus.setStyleSheet(u"QPushButton {	\n"
"	color: #fff;\n"
"	border-radius: 5px;\n"
"	padding: 2px;\n"
"	background-color: #476f95;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"	background-color: #43698a;	\n"
"}\n"
"\n"
"")
        self.gridLayout_28 = QGridLayout(self.pageStatus)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.Widget4 = QWidget(self.pageStatus)
        self.Widget4.setObjectName(u"Widget4")
        self.Widget4.setEnabled(True)
        self.gridLayout_21 = QGridLayout(self.Widget4)
        self.gridLayout_21.setSpacing(6)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(1, 1, -1, 1)
        self.frame_10 = QFrame(self.Widget4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(200, 0))
        self.frame_10.setMaximumSize(QSize(200, 16777215))
        self.frame_10.setStyleSheet(u"QFrame {\n"
"	background-color: #476f95;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"	\n"
"	border-bottom: 1px solid #ffffff;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 50, 0, 50)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 55))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_11)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QFrame {	\n"
"	border-radius: 5px;\n"
"	background-color: #d1dbe4;\n"
"\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_12)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setHorizontalSpacing(0)
        self.lineEdit4find = QLineEdit(self.frame_12)
        self.lineEdit4find.setObjectName(u"lineEdit4find")
        self.lineEdit4find.setFont(font)
        self.lineEdit4find.setStyleSheet(u"QLineEdit {\n"
"	background-color: #d1dbe4\n"
"}")
        self.lineEdit4find.setFrame(False)

        self.gridLayout_24.addWidget(self.lineEdit4find, 0, 2, 1, 1)

        self.widget_6 = QWidget(self.frame_12)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(25, 25))
        self.widget_6.setStyleSheet(u"")
        self.gridLayout_25 = QGridLayout(self.widget_6)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(3, 3, 3, 3)
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(25, 25))
        self.label_5.setStyleSheet(u"image: url(:/icon/Static/icons8-\u043f\u043e\u0438\u0441\u043a-50.png);")

        self.gridLayout_25.addWidget(self.label_5, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.widget_6, 0, 1, 1, 1)


        self.gridLayout_23.addLayout(self.gridLayout_24, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.frame_12, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_11)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_10)

        self.button4back = QPushButton(self.frame_10)
        self.button4back.setObjectName(u"button4back")
        self.button4back.setFont(font2)
        self.button4back.setLayoutDirection(Qt.LeftToRight)
        self.button4back.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.button4back)


        self.gridLayout_21.addWidget(self.frame_10, 0, 1, 1, 1)

        self.frame_14 = QFrame(self.Widget4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_14)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(100, 25, 100, 50)
        self.listWidget4status = QListWidget(self.frame_14)
        self.listWidget4status.setObjectName(u"listWidget4status")
        self.listWidget4status.setMinimumSize(QSize(250, 0))
        self.listWidget4status.setFont(font3)
        self.listWidget4status.setStyleSheet(u"QListWidget {\n"
"	padding: 5px;\n"
"	background-color: #fff;\n"
"	border: 1px solid #194a7a;\n"
"	border-radius: 4px;\n"
"}\n"
"")

        self.gridLayout_27.addWidget(self.listWidget4status, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frame_14, 0, 3, 1, 1)


        self.gridLayout_28.addWidget(self.Widget4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageStatus)
        self.pageLearn = QWidget()
        self.pageLearn.setObjectName(u"pageLearn")
        self.pageLearn.setStyleSheet(u"QPushButton {	\n"
"	color: #fff;\n"
"	border-radius: 5px;\n"
"	padding: 2px;\n"
"	background-color: #476f95;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"	background-color: #43698a;	\n"
"}")
        self.gridLayout_35 = QGridLayout(self.pageLearn)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.frame_15 = QFrame(self.pageLearn)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_15)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(25, 25, 0, 50)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_16)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(100, -1, 100, -1)
        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setVerticalSpacing(20)
        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setHorizontalSpacing(9)
        self.gridLayout_33.setVerticalSpacing(0)
        self.gridLayout_33.setContentsMargins(0, -1, 0, -1)
        self.lineEdit5translate = QLineEdit(self.frame_16)
        self.lineEdit5translate.setObjectName(u"lineEdit5translate")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit5translate.sizePolicy().hasHeightForWidth())
        self.lineEdit5translate.setSizePolicy(sizePolicy1)
        self.lineEdit5translate.setMinimumSize(QSize(180, 30))
        self.lineEdit5translate.setMaximumSize(QSize(200, 16777215))
        self.lineEdit5translate.setFont(font)
        self.lineEdit5translate.setFrame(True)

        self.gridLayout_33.addWidget(self.lineEdit5translate, 1, 1, 1, 1)

        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy2)
        self.frame_17.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setPointSize(12)
        self.frame_17.setFont(font4)
        self.frame_17.setStyleSheet(u"background-color: #fff;\n"
"	\n"
"")
        self.frame_17.setFrameShape(QFrame.Box)
        self.frame_17.setFrameShadow(QFrame.Plain)
        self.frame_17.setLineWidth(1)
        self.gridLayout_34 = QGridLayout(self.frame_17)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setVerticalSpacing(0)
        self.gridLayout_34.setContentsMargins(9, 0, -1, 0)
        self.label5word = QLabel(self.frame_17)
        self.label5word.setObjectName(u"label5word")
        sizePolicy1.setHeightForWidth(self.label5word.sizePolicy().hasHeightForWidth())
        self.label5word.setSizePolicy(sizePolicy1)
        self.label5word.setMinimumSize(QSize(100, 28))
        self.label5word.setMaximumSize(QSize(16777215, 28))
        font5 = QFont()
        font5.setFamilies([u"Tahoma"])
        font5.setPointSize(11)
        self.label5word.setFont(font5)
        self.label5word.setStyleSheet(u"background-color: #fff;")

        self.gridLayout_34.addWidget(self.label5word, 0, 0, 1, 1)


        self.gridLayout_33.addWidget(self.frame_17, 1, 0, 1, 1)

        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label5message = QLabel(self.frame_16)
        self.label5message.setObjectName(u"label5message")
        self.label5message.setMinimumSize(QSize(100, 10))
        self.label5message.setStyleSheet(u"")

        self.gridLayout_26.addWidget(self.label5message, 0, 0, 1, 1)


        self.gridLayout_33.addLayout(self.gridLayout_26, 0, 1, 1, 1)


        self.gridLayout_31.addLayout(self.gridLayout_33, 0, 0, 1, 1)

        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setHorizontalSpacing(12)
        self.gridLayout_32.setVerticalSpacing(6)
        self.gridLayout_32.setContentsMargins(0, -1, 0, -1)
        self.button5check = QPushButton(self.frame_16)
        self.button5check.setObjectName(u"button5check")
        self.button5check.setMinimumSize(QSize(100, 30))
        self.button5check.setFont(font)

        self.gridLayout_32.addWidget(self.button5check, 0, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.button5finish = QPushButton(self.frame_16)
        self.button5finish.setObjectName(u"button5finish")
        self.button5finish.setMinimumSize(QSize(100, 30))
        self.button5finish.setFont(font)

        self.gridLayout_32.addWidget(self.button5finish, 0, 1, 1, 1)


        self.gridLayout_31.addLayout(self.gridLayout_32, 1, 0, 1, 1)


        self.gridLayout_30.addLayout(self.gridLayout_31, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)


        self.gridLayout_29.addWidget(self.frame_16, 1, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_29.addItem(self.verticalSpacer_11, 2, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_29.addItem(self.verticalSpacer_12, 0, 0, 1, 1)


        self.gridLayout_35.addWidget(self.frame_15, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageLearn)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"English Eagle", None))
        self.button1exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.button1add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043b\u043e\u0432\u043e", None))
        self.button1edit.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.button1status.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.button1learn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0438\u0442\u044c \u0441\u043b\u043e\u0432\u0430", None))
        self.button2back.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.button2addword.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.lineEdit2addEnglish.setPlaceholderText(QCoreApplication.translate("MainWindow", u"English", None))
        self.lineEdit2addRussian.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Translate", None))
#if QT_CONFIG(tooltip)
        self.label2green_mark.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label2green_mark.setText("")
        self.label2message.setText("")
        self.button3delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.button3change.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.lineEdit3find.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label_4.setText("")
        self.lineEdit3reEnglish.setPlaceholderText(QCoreApplication.translate("MainWindow", u"English", None))
        self.lineEdit3reRussian.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Russian", None))
        self.button3save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.button3back.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.lineEdit4find.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label_5.setText("")
        self.button4back.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.lineEdit5translate.setText("")
        self.lineEdit5translate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.label5word.setText("")
        self.label5message.setText("")
        self.button5check.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.button5finish.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u043e\u043d\u0447\u0438\u0442\u044c", None))
    # retranslateUi

