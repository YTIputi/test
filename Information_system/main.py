from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QMenu, QDialog
from Information_system.Open import Ui_MainWindow
from Information_system.Register import Ui_Form
import json, os, string, datetime
from Information_system.Admin import Ui_MainWindow_1
from Information_system.Mened import Ui_MainWindow_2
from Information_system.Stock import Ui_MainWindow_3
from PySide6.QtCore import Qt
from Admin_role import Ui_Dialog


class Adm_D(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.flag = None

        self.ui.buttonGroup.buttonClicked.connect(self.choose)

    def choose(self, but):
        self.flag = but.text()
        self.ui.label.setText(f'Выбранная роль: {but.text()}')


class Open(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        with open(os.path.join(os.getcwd(), 'people.json')) as file:
            self.data = json.load(file)

        self.ui.pushButton_2.clicked.connect(self.go)
        self.ui.pushButton.clicked.connect(self.reg)

    def reg(self):
        self.w1 = Register()
        self.w1.show()

    def go(self):
        for person in self.data:
            if person['login'] != self.ui.lineEdit.text():
                self.ui.label_4.setText('Неверный логин')
                self.ui.label_4.setStyleSheet('QLabel {color: red;}')
            if person['password'] != self.ui.lineEdit_2.text():
                self.ui.label_5.setText('Неверный пароль')
                self.ui.label_5.setStyleSheet('QLabel {color: red;}')
            if person['login'] == self.ui.lineEdit.text() and person['password'] == self.ui.lineEdit_2.text():
                if person['title'] == 'admin':
                    self.w1 = Admin()
                    self.w1.show()
                    self.close()
                elif person['title'] == 'mened':
                    self.w1 = Mened()
                    self.w1.show()
                    self.close()
                elif person['title'] == 'stock':
                    self.w1 = Stock()
                    self.w1.show()
                    self.close()


class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.data = {}
        self.flag = [0] * 5
        self.ui.lineEdit.textChanged.connect(self.login)
        self.ui.lineEdit_2.textChanged.connect(self.password)
        self.ui.lineEdit_3.textChanged.connect(self.repeat_password)
        self.ui.lineEdit_4.textChanged.connect(self.email)
        self.ui.lineEdit_5.textChanged.connect(self.number)
        self.ui.lineEdit_6.textChanged.connect(self.name)
        self.ui.lineEdit_7.textChanged.connect(self.city)
        self.ui.lineEdit_8.textChanged.connect(self.about)
        self.ui.pushButton.clicked.connect(self.press)

    def login(self, text):
        if set(text) & set(string.ascii_letters) and 5 <= len(text):
            self.ui.label_10.setText('Логин подходит')
            self.ui.label_10.setStyleSheet('QLabel {color: green;}')
            self.flag[0] = 1
        else:
            self.ui.label_10.setText('Логин должен состоять из латинских букв и >= 5 символов')
            self.ui.label_10.setStyleSheet('QLabel {color: red;}')
            self.flag[0] = 0

    def password(self, text):
        if set(text) & set(string.ascii_letters) and 5 <= len(text):
            self.ui.label_12.setText('Пароль подходит')
            self.ui.label_12.setStyleSheet('QLabel {color: green;}')
            self.flag[1] = 1
        else:
            self.ui.label_12.setText('Пароль должен состоять из латинских букв и >= 5 символов')
            self.ui.label_12.setStyleSheet('QLabel {color: red;}')
            self.flag[1] = 0

    def repeat_password(self, text):
        if text == self.ui.lineEdit_2.text() and text:
            self.ui.label_11.setText('Пароль подходит')
            self.ui.label_11.setStyleSheet('QLabel {color: green;}')
            self.flag[2] = 1
        else:
            self.flag[2] = 0

    def email(self, text):
        if text[0] != '@' and text[-1] != '@' and '@' in text:
            self.ui.label_13.setText('Email подходит')
            self.ui.label_13.setStyleSheet('QLabel {color: green;}')
            self.flag[3] = 1
        else:
            self.ui.label_13.setText('Email должен содержать @ и не должен начинаться и заканчиваться @')
            self.ui.label_13.setStyleSheet('QLabel {color: red;}')
            self.flag[3] = 0

    def number(self, text):
        if len(text) == 11 and text[0] == '8' or len(text) == 12 and text[:2] == '+7':
            self.ui.label_14.setText('Телефонный номер подходит')
            self.ui.label_14.setStyleSheet('QLabel {color: green;}')
            self.flag[4] = 1
        else:
            self.ui.label_14.setText('Телефонный номер должен начинаться с 8 или +7')
            self.ui.label_14.setStyleSheet('QLabel {color: red;}')
            self.flag[4] = 0

    def name(self, text):
        pass

    def city(self, text):
        pass

    def about(self, text):
        pass

    def press(self):
        if sum(self.flag) == 5:
            self.data = {'login': f'{self.ui.lineEdit.text()}',
                         'password': f'{self.ui.lineEdit_2.text()}',
                         'email': f'{self.ui.lineEdit_3.text()}',
                         'number': f'{self.ui.lineEdit_5.text()}',
                         'name': f'{self.ui.lineEdit_6.text()}',
                         'city': f'{self.ui.lineEdit_7.text()}',
                         'about': f'{self.ui.lineEdit_8.text()}',
                         'data': f'{datetime.datetime.now()}'}

            with open(os.path.join(os.getcwd(), 'pred_people.json')) as file1:
                lis = json.load(file1)
                lis.append(self.data)
            with open(os.path.join(os.getcwd(), 'pred_people.json'), 'w') as file2:
                json.dump(lis, file2, indent=2)
            self.close()


class Admin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_1()
        self.ui.setupUi(self)
        with open(os.path.join(os.getcwd(), 'pred_people.json')) as file1:
            self.pred_data = json.load(file1)
        headers = ['id', 'name', 'data']
        for i in range(len(self.pred_data)):
            for j in range(len(headers)):
                if headers[j] == 'id':
                    self.ui.tableWidget.insertRow(i)
                    self.ui.tableWidget_2.insertRow(i)
                    item = QTableWidgetItem(f'{i + 1}')
                    self.ui.tableWidget.setItem(i, j, item)
                else:
                    item = QTableWidgetItem(f'{self.pred_data[i][headers[j]]}')
                    self.ui.tableWidget.setItem(i, j, item)

        self.table1 = self.ui.tableWidget
        self.table2 = self.ui.tableWidget_2

        self.table1.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table1.customContextMenuRequested.connect(self.context_menu)

    def context_menu(self, pos):
        self.pos = pos
        globalPos = self.table1.mapToGlobal(pos)
        context_menu = QMenu(self)
        action = context_menu.addAction("Переместить строку во вторую таблицу")
        selected_action = context_menu.exec(globalPos)
        if selected_action == action:
            self.win = Adm_D()
            self.win.show()
            self.win.ui.pushButton.clicked.connect(self.good)

    def good(self):
        if self.win.flag is not None:
            row = self.table1.currentRow()
            column = self.table1.currentColumn()
            s = 0
            for i in range(3):
                item0 = self.table1.item(row, i).text()
                if item0:
                    s += 1
            if s == 3:
                self.table1.setItem(row, column, QTableWidgetItem(self.win.flag))
                item = self.table1.itemAt(self.pos)
                if item is not None:
                    row = item.row()
                    for column in range(self.table1.columnCount()):
                        item = self.table1.item(row, column)
                        if item is not None:
                            self.table2.setItem(row, column, QTableWidgetItem(item.text()))
                            self.table1.setItem(row, column, QTableWidgetItem(""))
            self.win.close()


class Mened(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_2()
        self.ui.setupUi(self)


class Stock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_3()
        self.ui.setupUi(self)

app = QApplication()
w = Open()
w.show()
app.exec()