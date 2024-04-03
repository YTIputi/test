from PySide6.QtWidgets import QRadioButton, QCheckBox, QMainWindow, QApplication
from lunche import Ui_mainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Загружаю проект
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.count = [0] * 12
        self.count0 = 0

        self.ui.pushButton.setEnabled(False)

        self.ui.radioButton.clicked.connect(self.check1)
        self.ui.radioButton_2.clicked.connect(self.check1)
        self.ui.checkBox.clicked.connect(self.box1)
        self.ui.radioButton.setEnabled(False)
        self.ui.radioButton_2.setEnabled(False)

        self.ui.radioButton_3.clicked.connect(self.check2)
        self.ui.radioButton_4.clicked.connect(self.check2)
        self.ui.checkBox_2.clicked.connect(self.box2)
        self.ui.radioButton_3.setEnabled(False)
        self.ui.radioButton_4.setEnabled(False)

        self.ui.radioButton_5.clicked.connect(self.check3)
        self.ui.radioButton_6.clicked.connect(self.check3)
        self.ui.checkBox_3.clicked.connect(self.box3)
        self.ui.radioButton_5.setEnabled(False)
        self.ui.radioButton_6.setEnabled(False)

        self.ui.radioButton_7.clicked.connect(self.check4)
        self.ui.radioButton_8.clicked.connect(self.check4)
        self.ui.checkBox_4.clicked.connect(self.box4)
        self.ui.radioButton_7.setEnabled(False)
        self.ui.radioButton_8.setEnabled(False)

        self.ui.radioButton_9.clicked.connect(self.check5)
        self.ui.radioButton_10.clicked.connect(self.check5)
        self.ui.checkBox_5.clicked.connect(self.box5)
        self.ui.radioButton_9.setEnabled(False)
        self.ui.radioButton_10.setEnabled(False)

        self.ui.radioButton_11.clicked.connect(self.check6)
        self.ui.radioButton_12.clicked.connect(self.check6)
        self.ui.checkBox_6.clicked.connect(self.box6)
        self.ui.radioButton_11.setEnabled(False)
        self.ui.radioButton_12.setEnabled(False)

    def check1(self):
        if self.ui.radioButton.isChecked():
            self.count[0] = 1
            self.count[1] = 0
        else:
            self.count[0] = 0
            self.count[1] = 1
        if sum(self.count) >= 2 and self.count0 >= 2:
            self.ui.pushButton.setEnabled(True)

    def box1(self):
        if self.ui.checkBox.isChecked():
            self.count0 += 1
            self.ui.radioButton.setEnabled(True)
            self.ui.radioButton_2.setEnabled(True)
            if sum(self.count) >= 2 and self.count0 >= 2:
                self.ui.pushButton.setEnabled(True)
        else:
            self.count0 -= 1
            self.count[0] = 0
            self.count[1] = 0
            self.ui.radioButton.setEnabled(False)
            self.ui.radioButton_2.setEnabled(False)
            if sum(self.count) < 2 or self.count0 < 2:
                self.ui.pushButton.setEnabled(False)


    def check2(self):
        if self.ui.radioButton_3.isChecked():
            self.count[2] = 1
            self.count[3] = 0
        else:
            self.count[2] = 0
            self.count[3] = 1
        if sum(self.count) >= 2 and self.count0 >= 2:
            self.ui.pushButton.setEnabled(True)

    def box2(self):
        if self.ui.checkBox_2.isChecked():
            self.count0 += 1
            self.ui.radioButton_3.setEnabled(True)
            self.ui.radioButton_4.setEnabled(True)
            if sum(self.count) >= 2 and self.count0 >= 2:
                self.ui.pushButton.setEnabled(True)
        else:
            self.count0 -= 1
            self.count[2] = 0
            self.count[3] = 0
            self.ui.radioButton_3.setEnabled(False)
            self.ui.radioButton_4.setEnabled(False)
            if sum(self.count) < 2 or self.count0 < 2:
                self.ui.pushButton.setEnabled(False)


    def check3(self):
        if self.ui.radioButton_5.isChecked():
            self.count[4] = 1
            self.count[5] = 0
        else:
            self.count[4] = 0
            self.count[5] = 1
        if sum(self.count) >= 2 and self.count0 >= 2:
            self.ui.pushButton.setEnabled(True)

    def box3(self):
        if self.ui.checkBox_3.isChecked():
            self.count0 += 1
            self.ui.radioButton_5.setEnabled(True)
            self.ui.radioButton_6.setEnabled(True)
            if sum(self.count) >= 2 and self.count0 >= 2:
                self.ui.pushButton.setEnabled(True)
        else:
            self.count0 -= 1
            self.count[4] = 0
            self.count[5] = 0
            self.ui.radioButton_5.setEnabled(False)
            self.ui.radioButton_6.setEnabled(False)
            if sum(self.count) < 2 or self.count0 < 2:
                self.ui.pushButton.setEnabled(False)


    def check4(self):
        if self.ui.radioButton_7.isChecked():
            self.count[6] = 1
            self.count[7] = 0
        else:
            self.count[6] = 0
            self.count[7] = 1
        if sum(self.count) >= 2 and self.count0 >= 2:
            self.ui.pushButton.setEnabled(True)

    def box4(self):
        if self.ui.checkBox_4.isChecked():
            self.count0 += 1
            self.ui.radioButton_7.setEnabled(True)
            self.ui.radioButton_8.setEnabled(True)
            if sum(self.count) >= 2 and self.count0 >= 2:
                self.ui.pushButton.setEnabled(True)
        else:
            self.count0 -= 1
            self.count[6] = 0
            self.count[7] = 0
            self.ui.radioButton_7.setEnabled(False)
            self.ui.radioButton_8.setEnabled(False)
            if sum(self.count) < 2 or self.count0 < 2:
                self.ui.pushButton.setEnabled(False)


    def check5(self):
        if self.ui.radioButton_9.isChecked():
            self.count[8] = 1
            self.count[9] = 0
        else:
            self.count[8] = 0
            self.count[9] = 1
        if sum(self.count) >= 2 and self.count0 >= 2:
            self.ui.pushButton.setEnabled(True)

    def box5(self):
        if self.ui.checkBox_5.isChecked():
            self.count0 += 1
            self.ui.radioButton_9.setEnabled(True)
            self.ui.radioButton_10.setEnabled(True)
            if sum(self.count) >= 2 and self.count0 >= 2:
                self.ui.pushButton.setEnabled(True)
        else:
            self.count0 -= 1
            self.count[8] = 0
            self.count[9] = 0
            self.ui.radioButton_9.setEnabled(False)
            self.ui.radioButton_10.setEnabled(False)
            if sum(self.count) < 2 or self.count0 < 2:
                self.ui.pushButton.setEnabled(False)


    def check6(self):
        if self.ui.radioButton_11.isChecked():
            self.count[10] = 1
            self.count[11] = 0
        else:
            self.count[10] = 0
            self.count[11] = 1
        if sum(self.count) >= 2 and self.count0 >= 2:
            self.ui.pushButton.setEnabled(True)

    def box6(self):
        if self.ui.checkBox_6.isChecked():
            self.count0 += 1
            self.ui.radioButton_11.setEnabled(True)
            self.ui.radioButton_12.setEnabled(True)
            if sum(self.count) >= 2 and self.count0 >= 2:
                self.ui.pushButton.setEnabled(True)
        else:
            self.count0 -= 1
            self.count[10] = 0
            self.count[11] = 0
            self.ui.radioButton_11.setEnabled(False)
            self.ui.radioButton_12.setEnabled(False)
            if sum(self.count) < 2 or self.count0 < 2:
                self.ui.pushButton.setEnabled(False)


app = QApplication(sys.argv)
window0 = MainWindow()
window0.show()
app.exec()
