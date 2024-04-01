from PySide6.QtWidgets import QRadioButton, QCheckBox, QMainWindow, QApplication
from lunche import Ui_mainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Загружаю проект
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.count = 0

        # Блокирую QRadioButton
        self.ui.layoutWidget.setEnabled(False)
        self.ui.layoutWidget1.setEnabled(False)
        self.ui.layoutWidget2.setEnabled(False)
        self.ui.layoutWidget3.setEnabled(False)
        self.ui.layoutWidget4.setEnabled(False)
        self.ui.layoutWidget5.setEnabled(False)

        # Блокирую QPushButton
        self.ui.pushButton.setEnabled(False)

        # Проверяю состояние QCheckBox
        self.ui.checkBox.stateChanged.connect(self.block1)
        self.ui.checkBox_2.stateChanged.connect(self.block2)
        self.ui.checkBox_3.stateChanged.connect(self.block3)
        self.ui.checkBox_4.stateChanged.connect(self.block4)
        self.ui.checkBox_5.stateChanged.connect(self.block5)
        self.ui.checkBox_6.stateChanged.connect(self.block6)

    def block1(self, s):
        self.ui.layoutWidget.setEnabled(s)
        self.count += s - 1
        if self.count >= 2:
            self.ui.pushButton.setEnabled(True)
    def block2(self, s):
        self.ui.layoutWidget1.setEnabled(s)
        self.count += s - 1
        if self.count >= 2:
            self.ui.pushButton.setEnabled(True)
        else:
            self.ui.pushButton.setEnabled(False)
    def block3(self, s):
        self.ui.layoutWidget2.setEnabled(s)
        self.count += s - 1
        if self.count >= 2:
            self.ui.pushButton.setEnabled(True)
        else:
            self.ui.pushButton.setEnabled(False)
    def block4(self, s):
        self.ui.layoutWidget3.setEnabled(s)
        self.count += s - 1
        if self.count >= 2:
            self.ui.pushButton.setEnabled(True)
        else:
            self.ui.pushButton.setEnabled(False)
    def block5(self, s):
        self.ui.layoutWidget4.setEnabled(s)
        self.count += s - 1
        if self.count >= 2:
            self.ui.pushButton.setEnabled(True)
        else:
            self.ui.pushButton.setEnabled(False)
    def block6(self, s):
        self.ui.layoutWidget5.setEnabled(s)
        self.count += s - 1
        if self.count >= 2:
            self.ui.pushButton.setEnabled(True)
        else:
            self.ui.pushButton.setEnabled(False)



app = QApplication(sys.argv)
window0 = MainWindow()
window0.show()
app.exec()
