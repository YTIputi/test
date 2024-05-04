from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys, json, os
from untitled import Ui_MainWindow
from plan import Ui_MainWindow1


class Plan(QMainWindow):
    def __init__(self, question, person):
        super().__init__()
        if not os.path.isdir('../results_plan'):
            os.mkdir('../results_plan')
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)
        self.question = question
        self.person = person
        self.data = {self.person: {'positive': [], 'negative': [], 'count_positive': 0, 'count_negative': 0}}
        self.ui.label.setText(question)

        self.ui.lineEdit.textEdited.connect(self.argument)
        self.ui.pushButton.clicked.connect(self.positive)
        self.ui.pushButton_2.clicked.connect(self.negative)
        self.ui.pushButton_3.clicked.connect(self.save)


    def argument(self):
        if self.ui.lineEdit.text():
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_2.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
        else:
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton_2.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)

    def positive(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('Внимание')
        dlg.setText('Вы уверены, в своем решение?')
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            self.data[self.person]['count_positive'] += 1
            self.data[self.person]['positive'].append(self.ui.lineEdit.text())
            self.ui.listWidget.addItem(self.data[self.person]['positive'][-1])
            self.ui.lcdNumber.display(self.data[self.person]['count_positive'])

    def negative(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('Внимание')
        dlg.setText('Вы уверены, в своем решение?')
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            self.data[self.person]['count_negative'] += 1
            self.data[self.person]['negative'].append(self.ui.lineEdit.text())
            self.ui.listWidget_2.addItem(self.data[self.person]['negative'][-1])
            self.ui.lcdNumber_2.display(self.data[self.person]['count_negative'])

    def save(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('Внимание')
        dlg.setText('Вы уверены, в своем решение?')
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            with open(os.path.join('../results_plan', f'{self.question}.json'), 'w') as file:
                json.dump(self.data, file, indent=2)


class Question(QMainWindow):
    def __init__(self, person):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.person = person

        self.ui.lineEdit.returnPressed.connect(self.question)

    def question(self):
        self.ui.tabWidget.addTab(Plan(self.ui.lineEdit.text(), self.person), self.ui.lineEdit.text())


