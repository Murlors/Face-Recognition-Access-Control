# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'record.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_record(object):
    def setupUi(self, record):
        if not record.objectName():
            record.setObjectName(u"record")
        record.resize(960, 640)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        font.setBold(True)
        record.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        record.setWindowIcon(icon)
        record.setStyleSheet(u"")
        self.mainbgftame = QFrame(record)
        self.mainbgftame.setObjectName(u"mainbgftame")
        self.mainbgftame.setGeometry(QRect(0, 0, 960, 640))
        self.mainbgftame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.165, x2:1, y2:0.449, stop:0 rgba(201, 201, 201, 255), stop:1 rgba(1, 29, 63, 255));\n"
"border-top-left-radius:50px;\n"
"border-bottom-right-radius:50px;")
        self.mainbgftame.setFrameShape(QFrame.StyledPanel)
        self.mainbgftame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget_3 = QWidget(self.mainbgftame)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(640, 10, 241, 61))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(54, 120, 182);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.timelabel = QLabel(self.horizontalLayoutWidget_3)
        self.timelabel.setObjectName(u"timelabel")
        self.timelabel.setFont(font)
        self.timelabel.setStyleSheet(u"background-color: rgb(54, 120, 182);\n"
"color: rgb(255, 255, 255);")
        self.timelabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.timelabel)

        self.horizontalLayoutWidget_6 = QWidget(self.mainbgftame)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(640, 80, 241, 61))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.horizontalLayoutWidget_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background-color: rgb(54, 120, 182);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.datelabel = QLabel(self.horizontalLayoutWidget_6)
        self.datelabel.setObjectName(u"datelabel")
        self.datelabel.setFont(font)
        self.datelabel.setStyleSheet(u"background-color: rgb(54, 120, 182);\n"
"color: rgb(255, 255, 255);")
        self.datelabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.datelabel)

        self.groupBox = QGroupBox(self.mainbgftame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 140, 881, 111))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"background-color:none;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Submitbutton = QPushButton(self.groupBox)
        self.Submitbutton.setObjectName(u"Submitbutton")
        self.Submitbutton.setGeometry(QRect(610, 40, 241, 41))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.Submitbutton.setFont(font2)
        self.Submitbutton.setStyleSheet(u"QPushButton#Submitbutton{\n"
"border:5px ;\n"
"	background-color: rgb(2, 108, 203);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#Submitbutton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(52, 73, 98), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#Submitbutton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(150,123,111);}")
        self.Submitbutton.setCheckable(True)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 20, 49, 81))
        self.label_3.setFont(font)
        self.idEdit = QLineEdit(self.groupBox)
        self.idEdit.setObjectName(u"idEdit")
        self.idEdit.setGeometry(QRect(130, 50, 150, 22))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(328, 20, 61, 81))
        self.label_4.setFont(font)
        self.dateEdit_end = QDateEdit(self.groupBox)
        self.dateEdit_end.setObjectName(u"dateEdit_end")
        self.dateEdit_end.setGeometry(QRect(390, 60, 150, 22))
        self.dateEdit_end.setDateTime(QDateTime(QDate(2022, 12, 25), QTime(0, 0, 0)))
        self.dateEdit_end.setMaximumDate(QDate(9998, 12, 31))
        self.dateEdit_end.setCalendarPopup(True)
        self.dateEdit_end.setTimeSpec(Qt.UTC)
        self.dateEdit_begin = QDateEdit(self.groupBox)
        self.dateEdit_begin.setObjectName(u"dateEdit_begin")
        self.dateEdit_begin.setGeometry(QRect(390, 30, 150, 22))
        self.dateEdit_begin.setDateTime(QDateTime(QDate(2022, 12, 24), QTime(16, 0, 0)))
        self.dateEdit_begin.setMaximumDate(QDate(9998, 12, 31))
        self.dateEdit_begin.setCalendarPopup(True)
        self.dateEdit_begin.setTimeSpec(Qt.UTC)
        self.tableWidget = QTableWidget(self.mainbgftame)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(54, 120, 182));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        __qtablewidgetitem1.setBackground(QColor(54, 120, 182));
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        __qtablewidgetitem2.setBackground(QColor(54, 120, 182));
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        __qtablewidgetitem3.setBackground(QColor(54, 120, 182));
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 250, 870, 350))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"\n"
"border:1px solid;\n"
"border-top-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"")
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(135)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(214)
        self.tableWidget.verticalHeader().setMinimumSectionSize(50)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.backbutton = QPushButton(record)
        self.backbutton.setObjectName(u"backbutton")
        self.backbutton.setGeometry(QRect(30, 20, 101, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backbutton.sizePolicy().hasHeightForWidth())
        self.backbutton.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.backbutton.setFont(font3)
        self.backbutton.setStyleSheet(u"QPushButton#backbutton{\n"
"border:5px ;\n"
"	background-color: rgb(2, 108, 203);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#backbutton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(52, 73, 98), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#backbutton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(150,123,111);}")
        icon1 = QIcon()
        icon1.addFile(u"back.png", QSize(), QIcon.Selected, QIcon.On)
        self.backbutton.setIcon(icon1)

        self.retranslateUi(record)

        QMetaObject.connectSlotsByName(record)
    # setupUi

    def retranslateUi(self, record):
        record.setWindowTitle(QCoreApplication.translate("record", u"History", None))
        self.label_7.setText(QCoreApplication.translate("record", u"Time :", None))
        self.timelabel.setText(QCoreApplication.translate("record", u"-", None))
        self.label_9.setText(QCoreApplication.translate("record", u"Date :", None))
        self.datelabel.setText(QCoreApplication.translate("record", u"-", None))
        self.groupBox.setTitle(QCoreApplication.translate("record", u"Details", None))
        self.Submitbutton.setText(QCoreApplication.translate("record", u"Submit", None))
        self.label_3.setText(QCoreApplication.translate("record", u"ID :", None))
        self.idEdit.setPlaceholderText(QCoreApplication.translate("record", u"UserID", None))
        self.label_4.setText(QCoreApplication.translate("record", u"Date:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("record", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("record", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("record", u"Time", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("record", u"Direction", None));
        self.backbutton.setText(QCoreApplication.translate("record", u"BACK", None))
    # retranslateUi

