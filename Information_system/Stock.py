# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Stock.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow_3(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(688, 472)
        MainWindow.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(218, 140, 44, 255), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgba(255, 255, 255, 76);")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(15)
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFont(font1)

        self.verticalLayout_2.addWidget(self.tableView)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_2.setFont(font2)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(15)
        font3.setBold(False)
        self.label_5.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tableView_2 = QTableView(self.widget)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setFont(font1)

        self.verticalLayout.addWidget(self.tableView_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)


        self.horizontalLayout_5.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 688, 31))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0435\u043c \u0442\u043e\u0432\u0430\u0440\u043e\u0432", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u044b\u0445:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043f\u0440\u0438\u043d\u044f\u044b\u0442\u0445:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u043e\u0432", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u0442\u043e\u0432\u0430\u0440\u043e\u0432:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043e\u0442\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u044b\u0445:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

