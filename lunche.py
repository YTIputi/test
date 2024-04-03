# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lunche.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(808, 705)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        font.setBold(False)
        mainWindow.setFont(font)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        font2 = QFont()
        font2.setPointSize(18)
        self.checkBox.setFont(font2)
        self.checkBox.setTabletTracking(False)
        self.checkBox.setIconSize(QSize(16, 16))
        self.checkBox.setChecked(False)
        self.checkBox.setAutoRepeat(False)
        self.checkBox.setAutoExclusive(False)

        self.verticalLayout_8.addWidget(self.checkBox)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")
        font3 = QFont()
        font3.setPointSize(16)
        self.radioButton.setFont(font3)

        self.verticalLayout_7.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font3)

        self.verticalLayout_7.addWidget(self.radioButton_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout_19.addLayout(self.verticalLayout_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_2 = QCheckBox(self.widget_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font2)

        self.verticalLayout_9.addWidget(self.checkBox_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButton_3 = QRadioButton(self.widget_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font3)

        self.verticalLayout_3.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.widget_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font3)

        self.verticalLayout_3.addWidget(self.radioButton_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)


        self.verticalLayout_10.addWidget(self.widget_2)


        self.verticalLayout_19.addLayout(self.verticalLayout_10)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.checkBox_3 = QCheckBox(self.widget_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font2)

        self.verticalLayout_11.addWidget(self.checkBox_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.radioButton_5 = QRadioButton(self.widget_3)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setFont(font3)

        self.verticalLayout_4.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.widget_3)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setFont(font3)

        self.verticalLayout_4.addWidget(self.radioButton_6)


        self.verticalLayout_11.addLayout(self.verticalLayout_4)


        self.verticalLayout_12.addWidget(self.widget_3)


        self.verticalLayout_19.addLayout(self.verticalLayout_12)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_13 = QVBoxLayout(self.widget_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.checkBox_4 = QCheckBox(self.widget_4)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font2)

        self.verticalLayout_13.addWidget(self.checkBox_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.radioButton_7 = QRadioButton(self.widget_4)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setFont(font3)

        self.verticalLayout_5.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.widget_4)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setFont(font3)

        self.verticalLayout_5.addWidget(self.radioButton_8)


        self.verticalLayout_13.addLayout(self.verticalLayout_5)


        self.verticalLayout_14.addWidget(self.widget_4)


        self.verticalLayout_19.addLayout(self.verticalLayout_14)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_15 = QVBoxLayout(self.widget_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.checkBox_5 = QCheckBox(self.widget_5)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font2)

        self.verticalLayout_15.addWidget(self.checkBox_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.radioButton_9 = QRadioButton(self.widget_5)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setFont(font3)

        self.verticalLayout_6.addWidget(self.radioButton_9)

        self.radioButton_10 = QRadioButton(self.widget_5)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setFont(font3)

        self.verticalLayout_6.addWidget(self.radioButton_10)


        self.verticalLayout_15.addLayout(self.verticalLayout_6)


        self.verticalLayout_16.addWidget(self.widget_5)


        self.verticalLayout_19.addLayout(self.verticalLayout_16)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_17 = QVBoxLayout(self.widget_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.checkBox_6 = QCheckBox(self.widget_6)
        self.checkBox_6.setObjectName(u"checkBox_6")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(18)
        self.checkBox_6.setFont(font4)

        self.verticalLayout_17.addWidget(self.checkBox_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_11 = QRadioButton(self.widget_6)
        self.radioButton_11.setObjectName(u"radioButton_11")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(16)
        self.radioButton_11.setFont(font5)

        self.verticalLayout.addWidget(self.radioButton_11)

        self.radioButton_12 = QRadioButton(self.widget_6)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setFont(font5)

        self.verticalLayout.addWidget(self.radioButton_12)


        self.verticalLayout_17.addLayout(self.verticalLayout)


        self.verticalLayout_18.addWidget(self.widget_6)


        self.verticalLayout_19.addLayout(self.verticalLayout_18)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font4)

        self.verticalLayout_19.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_19)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 808, 24))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u0410\u0441\u0441\u043e\u0440\u0442\u0438\u043c\u0435\u043d\u0442", None))
        self.checkBox.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0435\u0440\u0432\u043e\u0435", None))
        self.radioButton.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.radioButton_2.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.checkBox_2.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0442\u043e\u0440\u043e\u0435", None))
        self.radioButton_3.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.radioButton_4.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.checkBox_3.setText(QCoreApplication.translate("mainWindow", u"\u0413\u043e\u0440\u044f\u0447\u0435\u0435", None))
        self.radioButton_5.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.radioButton_6.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.checkBox_4.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0430\u043b\u0430\u0442\u044b", None))
        self.radioButton_7.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.radioButton_8.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.checkBox_5.setText(QCoreApplication.translate("mainWindow", u"\u0414\u0435\u0441\u0435\u0440\u0442\u044b", None))
        self.radioButton_9.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.radioButton_10.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.checkBox_6.setText(QCoreApplication.translate("mainWindow", u"\u041d\u0430\u043f\u0438\u0442\u043a\u0438", None))
        self.radioButton_11.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.radioButton_12.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u043a\u0430\u0437\u0430\u0442\u044c", None))
    # retranslateUi

