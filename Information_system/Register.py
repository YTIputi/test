# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(790, 763)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(15)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(125, 227, 140, 255), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgba(255, 255, 255, 75);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -269, 756, 1014))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.line_10 = QFrame(self.scrollAreaWidgetContents)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_10)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_2.addWidget(self.label_10)


        self.verticalLayout_9.addLayout(self.verticalLayout_2)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.lineEdit_2)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_3.addWidget(self.label_12)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout.addWidget(self.label_11)


        self.verticalLayout_9.addLayout(self.verticalLayout)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_4.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font)

        self.verticalLayout_4.addWidget(self.lineEdit_4)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_4.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.verticalLayout_4)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_5.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font)

        self.verticalLayout_5.addWidget(self.lineEdit_5)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_5.addWidget(self.label_14)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.line_7 = QFrame(self.scrollAreaWidgetContents)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_6.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font)

        self.verticalLayout_6.addWidget(self.lineEdit_6)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        self.line_8 = QFrame(self.scrollAreaWidgetContents)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_7.addWidget(self.label_8)

        self.lineEdit_7 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font)

        self.verticalLayout_7.addWidget(self.lineEdit_7)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.line_9 = QFrame(self.scrollAreaWidgetContents)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_8.addWidget(self.label_9)

        self.lineEdit_8 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setFont(font)

        self.verticalLayout_8.addWidget(self.lineEdit_8)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.line_11 = QFrame(self.scrollAreaWidgetContents)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_11)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.verticalLayout_9.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_9)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Register", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.label_10.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_12.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0432\u0442\u043e\u0440\u043d\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c \u043f\u043e\u0432\u0442\u043e\u0440\u043d\u043e", None))
        self.label_11.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0443\u044e \u043f\u043e\u0447\u0442\u0443", None))
        self.label_13.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.label_14.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0424\u0418\u041e", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u041e \u0441\u0435\u0431\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

