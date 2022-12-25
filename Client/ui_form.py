# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 640)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainbgftame = QFrame(self.centralwidget)
        self.mainbgftame.setObjectName(u"mainbgftame")
        self.mainbgftame.setGeometry(QRect(0, 0, 960, 640))
        self.mainbgftame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.165, x2:1, y2:0.449, stop:0 rgba(201, 201, 201, 255), stop:1 rgba(1, 29, 63, 255));\n"
"border-top-left-radius:50px;\n"
"border-bottom-right-radius:50px;")
        self.mainbgftame.setFrameShape(QFrame.StyledPanel)
        self.mainbgftame.setFrameShadow(QFrame.Raised)
        self.imgLabel = QLabel(self.mainbgftame)
        self.imgLabel.setObjectName(u"imgLabel")
        self.imgLabel.setGeometry(QRect(20, 60, 621, 481))
        self.imgLabel.setStyleSheet(u"border:10px solid  rgb(2, 108, 203);\n"
"border-top-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"")
        self.groupBox_2 = QGroupBox(self.mainbgftame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(650, 220, 291, 361))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(18)
        font.setBold(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget_4 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 40, 271, 271))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.gridLayoutWidget_4)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.statuslabel_2 = QLabel(self.gridLayoutWidget_4)
        self.statuslabel_2.setObjectName(u"statuslabel_2")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.statuslabel_2.setFont(font2)
        self.statuslabel_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.statuslabel_2)


        self.gridLayout_5.addLayout(self.horizontalLayout_11, 2, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.gridLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.namelabel_2 = QLabel(self.gridLayoutWidget_4)
        self.namelabel_2.setObjectName(u"namelabel_2")
        self.namelabel_2.setFont(font2)
        self.namelabel_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.namelabel_2)


        self.gridLayout_5.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.gridLayoutWidget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.timelabel_3 = QLabel(self.gridLayoutWidget_4)
        self.timelabel_3.setObjectName(u"timelabel_3")
        self.timelabel_3.setFont(font1)
        self.timelabel_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.timelabel_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.timelabel_3)


        self.gridLayout_5.addLayout(self.horizontalLayout_12, 3, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.gridLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.idlabel = QLabel(self.gridLayoutWidget_4)
        self.idlabel.setObjectName(u"idlabel")
        self.idlabel.setFont(font2)
        self.idlabel.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.idlabel)


        self.gridLayout_5.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.horizontalLayoutWidget_4 = QWidget(self.mainbgftame)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(680, 120, 241, 61))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.horizontalLayoutWidget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"background-color: rgb(54, 120, 182);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.timelabel_2 = QLabel(self.horizontalLayoutWidget_4)
        self.timelabel_2.setObjectName(u"timelabel_2")
        self.timelabel_2.setFont(font1)
        self.timelabel_2.setStyleSheet(u"background-color: rgb(54, 120, 182);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.timelabel_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.timelabel_2)

        self.horizontalLayoutWidget_7 = QWidget(self.mainbgftame)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(680, 50, 241, 61))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.horizontalLayoutWidget_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background-color: rgb(54, 120, 182);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_13)

        self.datelabel_2 = QLabel(self.horizontalLayoutWidget_7)
        self.datelabel_2.setObjectName(u"datelabel_2")
        self.datelabel_2.setFont(font1)
        self.datelabel_2.setStyleSheet(u"background-color: rgb(54, 120, 182);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.datelabel_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.datelabel_2)

        self.recordbutton = QPushButton(self.mainbgftame)
        self.recordbutton.setObjectName(u"recordbutton")
        self.recordbutton.setEnabled(True)
        self.recordbutton.setGeometry(QRect(670, 570, 245, 31))
        self.recordbutton.setFont(font1)
        self.recordbutton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.recordbutton.setCheckable(True)
        self.recordbutton.setAutoRepeat(True)
        self.recordbutton.setAutoDefault(False)
        self.recordbutton.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.recordbutton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.imgLabel.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.statuslabel_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.namelabel_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.timelabel_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ID :", None))
        self.idlabel.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Time :", None))
        self.timelabel_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.datelabel_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.recordbutton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u65e5\u5fd7", None))
    # retranslateUi

