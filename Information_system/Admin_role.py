# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Admin_role.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QDialog, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(412, 507)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(173, 123, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"padding: 5px;")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgba(255, 255, 255, 75);")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton = QRadioButton(self.widget)
        self.buttonGroup = QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(15)
        self.radioButton.setFont(font1)

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font1)

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.widget)
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font1)

        self.verticalLayout.addWidget(self.radioButton_3)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u0430\u044f \u0440\u043e\u043b\u044c: ", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"\u0421\u043a\u043b\u0430\u0434\u0441\u043a\u043a\u043e\u0439 \u0440\u0430\u0431\u043e\u0447\u0438\u0439", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

