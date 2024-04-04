from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget
import sys, os
from plan3 import Ui_mainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        if not os.path.isfile('result'):
            with open('result', 'w') as file:
                pass
        else:
            with open('result', encoding='utf-8') as file:
                for res in file.readlines():
                    res = eval(res.replace('\n', ''))
                    # self.ui.comboBox.addItem(res['question'])

        self.ui.lineEdit.setPlaceholderText('Введите вопрос')
        self.ui.lineEdit_2.setPlaceholderText('Введите аргумент')

        self.ui.lineEdit.returnPressed.connect(self.add_question)
        self.ui.pushButton.clicked.connect(self.add_argument_positive)
        self.ui.pushButton_2.clicked.connect(self.add_argument_negative)
        # self.ui.comboBox.currentIndexChanged.connect(self.choose)
        self.ui.pushButton_3.clicked.connect(self.save_data)
        self.ui.listWidget.currentItemChanged.connect(self.index_changed)
        self.ui.listWidget_2.currentItemChanged.connect(self.index_changed2)


    def add_question(self):
        if self.ui.lineEdit.text():
            if self.ui.checkBox.isChecked():
                self.ui.checkBox.setChecked(False)
            self.save = {}
            self.last1 = self.last2 = None
            self.ui.listWidget.clear()
            self.ui.listWidget_2.clear()
            self.ui.lcdNumber.display(0)
            self.ui.label.setText(f'Вопрос: {self.ui.lineEdit.text()}')
            self.save['question'] = self.ui.lineEdit.text()


    def add_argument_positive(self):
        if self.ui.lineEdit_2.text() and self.ui.label.text() and not self.ui.checkBox.isChecked():
            self.save['count'] = self.save.get('count', 0) + 1
            self.save['positive'] = self.save.get('positive', []) + [f'{self.ui.lineEdit_2.text()}']
            self.ui.listWidget.addItem(self.save['positive'][-1])
            self.ui.lcdNumber.display(self.save['count'])


    def add_argument_negative(self):
        if self.ui.lineEdit_2.text() and self.ui.label.text() and not self.ui.checkBox.isChecked():
            self.save['count'] = self.save.get('count', 0) + 1
            self.save['negative'] = self.save.get('negative', []) + [f'{self.ui.lineEdit_2.text()}']
            self.ui.listWidget_2.addItem(self.save['negative'][-1])
            self.ui.lcdNumber.display(self.save['count'])

    def save_data(self):
        if self.ui.lineEdit.text() and len(self.save) > 1:
            self.ui.tabWidget.addTab(QWidget(), self.ui.lineEdit.text())
            with open('result', 'a', encoding='utf-8') as file:
                file.write(f'{self.save}\n')
            self.last1 = self.last2 = None

    # def choose(self):
    #     with open('result', encoding='utf-8') as file:
    #         for res in file.readlines():
    #             res = eval(res.replace('\n', ''))
    #             if res['question'] == self.ui.comboBox.currentText():
    #                 self.ui.listWidget.clear()
    #                 self.ui.label.setText(res['question'])
    #                 self.ui.listWidget.addItems(res['positive'])
    #                 self.ui.listWidget_2.addItems(res['negative'])
    #                 self.ui.lcdNumber.display(res['count'])

    def index_changed(self, i):
        if self.ui.lcdNumber.digitCount() and not self.ui.checkBox.isChecked():
            if self.last1 is None:
                self.last1 = self.ui.listWidget.currentRow()

            else:
                now = self.ui.listWidget.currentRow()
                self.ui.listWidget.insertItem(now + 1, self.ui.listWidget.takeItem(self.last1))
                self.last1 = None

    def index_changed2(self, i):
        if self.ui.lcdNumber.digitCount() and not self.ui.checkBox.isChecked():
            if self.last2 is None:
                self.last2 = self.ui.listWidget_2.currentRow()

            else:
                now = self.ui.listWidget_2.currentRow()
                self.ui.listWidget_2.insertItem(now + 1, self.ui.listWidget_2.takeItem(self.last2))
                self.last2 = None


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

