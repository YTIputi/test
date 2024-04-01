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
    QSizePolicy, QSpacerItem, QSplitter, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(808, 701)
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

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.checkBox = QCheckBox(self.splitter_2)
        self.checkBox.setObjectName(u"checkBox")
        font2 = QFont()
        font2.setPointSize(18)
        self.checkBox.setFont(font2)
        self.checkBox.setTabletTracking(False)
        self.checkBox.setIconSize(QSize(16, 16))
        self.checkBox.setChecked(False)
        self.checkBox.setAutoRepeat(False)
        self.checkBox.setAutoExclusive(False)
        self.splitter_2.addWidget(self.checkBox)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(u"radioButton")
        font3 = QFont()
        font3.setPointSize(16)
        self.radioButton.setFont(font3)

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font3)

        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.splitter_2.addWidget(self.layoutWidget)

        self.verticalLayout_7.addWidget(self.splitter_2)

        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.checkBox_2 = QCheckBox(self.splitter_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font2)
        self.splitter_3.addWidget(self.checkBox_2)
        self.layoutWidget1 = QWidget(self.splitter_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.radioButton_4 = QRadioButton(self.layoutWidget1)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font3)

        self.verticalLayout_3.addWidget(self.radioButton_4)

        self.radioButton_3 = QRadioButton(self.layoutWidget1)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font3)

        self.verticalLayout_3.addWidget(self.radioButton_3)

        self.splitter_3.addWidget(self.layoutWidget1)

        self.verticalLayout_7.addWidget(self.splitter_3)

        self.splitter_4 = QSplitter(self.centralwidget)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.checkBox_3 = QCheckBox(self.splitter_4)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font2)
        self.splitter_4.addWidget(self.checkBox_3)
        self.layoutWidget2 = QWidget(self.splitter_4)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.radioButton_5 = QRadioButton(self.layoutWidget2)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setFont(font3)

        self.verticalLayout_4.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.layoutWidget2)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setFont(font3)

        self.verticalLayout_4.addWidget(self.radioButton_6)

        self.splitter_4.addWidget(self.layoutWidget2)

        self.verticalLayout_7.addWidget(self.splitter_4)

        self.splitter_5 = QSplitter(self.centralwidget)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Vertical)
        self.splitter_7 = QSplitter(self.splitter_5)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Vertical)
        self.splitter_9 = QSplitter(self.splitter_7)
        self.splitter_9.setObjectName(u"splitter_9")
        self.splitter_9.setOrientation(Qt.Vertical)
        self.checkBox_4 = QCheckBox(self.splitter_9)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font2)
        self.splitter_9.addWidget(self.checkBox_4)
        self.layoutWidget3 = QWidget(self.splitter_9)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.radioButton_8 = QRadioButton(self.layoutWidget3)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setFont(font3)

        self.verticalLayout_5.addWidget(self.radioButton_8)

        self.radioButton_7 = QRadioButton(self.layoutWidget3)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setFont(font3)

        self.verticalLayout_5.addWidget(self.radioButton_7)

        self.splitter_9.addWidget(self.layoutWidget3)
        self.splitter_7.addWidget(self.splitter_9)
        self.splitter_5.addWidget(self.splitter_7)

        self.verticalLayout_7.addWidget(self.splitter_5)

        self.splitter_6 = QSplitter(self.centralwidget)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Vertical)
        self.checkBox_5 = QCheckBox(self.splitter_6)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font2)
        self.splitter_6.addWidget(self.checkBox_5)
        self.layoutWidget4 = QWidget(self.splitter_6)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.radioButton_9 = QRadioButton(self.layoutWidget4)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setFont(font3)

        self.verticalLayout_6.addWidget(self.radioButton_9)

        self.radioButton_10 = QRadioButton(self.layoutWidget4)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setFont(font3)

        self.verticalLayout_6.addWidget(self.radioButton_10)

        self.splitter_6.addWidget(self.layoutWidget4)

        self.verticalLayout_7.addWidget(self.splitter_6)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter_8 = QSplitter(self.splitter)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setOrientation(Qt.Vertical)
        self.checkBox_6 = QCheckBox(self.splitter_8)
        self.checkBox_6.setObjectName(u"checkBox_6")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(18)
        self.checkBox_6.setFont(font4)
        self.splitter_8.addWidget(self.checkBox_6)
        self.layoutWidget5 = QWidget(self.splitter_8)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.verticalLayout = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_11 = QRadioButton(self.layoutWidget5)
        self.radioButton_11.setObjectName(u"radioButton_11")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(16)
        self.radioButton_11.setFont(font5)

        self.verticalLayout.addWidget(self.radioButton_11)

        self.radioButton_12 = QRadioButton(self.layoutWidget5)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setFont(font5)

        self.verticalLayout.addWidget(self.radioButton_12)

        self.splitter_8.addWidget(self.layoutWidget5)
        self.splitter.addWidget(self.splitter_8)

        self.verticalLayout_7.addWidget(self.splitter)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font4)

        self.verticalLayout_7.addWidget(self.pushButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

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
        self.radioButton_4.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.radioButton_3.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.checkBox_3.setText(QCoreApplication.translate("mainWindow", u"\u0413\u043e\u0440\u044f\u0447\u0435\u0435", None))
        self.radioButton_5.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.radioButton_6.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.checkBox_4.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0430\u043b\u0430\u0442\u044b", None))
        self.radioButton_8.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.radioButton_7.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.checkBox_5.setText(QCoreApplication.translate("mainWindow", u"\u0414\u0435\u0441\u0435\u0440\u0442\u044b", None))
        self.radioButton_9.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.radioButton_10.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.checkBox_6.setText(QCoreApplication.translate("mainWindow", u"\u041d\u0430\u043f\u0438\u0442\u043a\u0438", None))
        self.radioButton_11.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.radioButton_12.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u044e\u0434\u043e", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u043a\u0430\u0437\u0430\u0442\u044c", None))
    # retranslateUi

