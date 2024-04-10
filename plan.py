# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plan.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(False)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_9 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(30)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit = QLineEdit(self.widget_5)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_6.addWidget(self.lineEdit)

        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.pushButton.setFont(font2)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.line_6 = QFrame(self.widget_4)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_6)

        self.pushButton_2 = QPushButton(self.widget_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        self.pushButton_2.setFont(font3)

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.horizontalLayout_6.addWidget(self.widget_4)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lcdNumber = QLCDNumber(self.widget_7)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.horizontalLayout_2.addWidget(self.lcdNumber)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.widget_7)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)


        self.verticalLayout.addWidget(self.widget)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lcdNumber_2 = QLCDNumber(self.widget_6)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")

        self.horizontalLayout_3.addWidget(self.lcdNumber_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.listWidget_2 = QListWidget(self.widget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.horizontalLayout_4.addWidget(self.listWidget_2)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.pushButton_3)


        self.verticalLayout_3.addWidget(self.widget_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Plan", None))
        self.label.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0442\u0438\u0432", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0442\u0438\u0432", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

