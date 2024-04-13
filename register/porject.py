from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
import sys, os, json, string, zlib
from register.Open import Ui_MainWindow
from register.Register import Ui_Form


class Open(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.w = None

        if not os.path.isfile('people.json'):
            with open('people.json', 'w') as file:
                json.dump([{'login': 'gleb', 'password': '123'}])

        self.ui.pushButton_2.clicked.connect(self.pressed)
        self.ui.pushButton.clicked.connect(self.regist)

    def pressed(self):
        with open(os.path.join('register', 'people.json'), encoding='utf-8') as file:
            self.data = json.load(file)
            if self.data and any(person['login'] == self.ui.lineEdit.text() and person['password'] == zlib.crc32(self.ui.lineEdit_2.text().encode('utf-8')) for person in self.data):
                self.good = QMainWindow()
                self.good.show()
                self.close()
            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle('Не корректные данные')
                dlg.setText('Вы ввели не верный логин или пароль')
                dlg.setIcon(QMessageBox.Icon.NoIcon)
                dlg.exec()
    def regist(self):
        if self.w is None:
            self.w = Register()
        self.w.show()
        self.close()


class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.data = {'login': '', 'password': '', 'email': '', 'phone': '', 'name': '', 'city': '', 'about': ''}
        self.ui.lineEdit.returnPressed.connect(self.login_reg)
        self.ui.lineEdit_2.returnPressed.connect(self.password_reg)
        self.ui.lineEdit_3.returnPressed.connect(self.rep_password_reg)
        self.ui.lineEdit_4.returnPressed.connect(self.email_reg)
        self.ui.lineEdit_5.returnPressed.connect(self.phone_reg)
        self.ui.lineEdit_6.returnPressed.connect(self.name_reg)
        self.ui.lineEdit_7.returnPressed.connect(self.city_reg)
        self.ui.lineEdit_8.returnPressed.connect(self.about_reg)

    def check(self):
        print(self.data)
        if all(self.data[key] for key in self.data):
            with open(os.path.join('register', 'people.json')) as file:
                lis = json.load(file)
                lis.append(self.data)
            with open(os.path.join('register', 'people.json'), 'w') as file1:
                json.dump(lis, file1)

            self.good = QMainWindow()
            self.good.show()
            self.close()

    def dial(self, title, mistake):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(title)
        dlg.setText(mistake)
        dlg.setIcon(QMessageBox.Icon.NoIcon)
        dlg.exec()

    def login_reg(self):
        if len(self.ui.lineEdit.text()) >= 5 and not set(self.ui.lineEdit.text()) - (set(string.ascii_letters) | set(string.digits)):
            self.data['login'] = self.ui.lineEdit.text()
            self.check()
        else:
            self.dial('Не корректные данные', 'Логин состоит не менее чем из 5 символов из набора латинских букв и цифр')

    def password_reg(self):
        if len(self.ui.lineEdit_2.text()) >= 8 and all(set(self.ui.lineEdit_2.text()) & set(i) for i in [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]):
            self.data['password'] = zlib.crc32(self.ui.lineEdit_2.text().encode('utf-8'))
            self.check()
        else:
            self.dial('Не корректные данные', 'Пароль должен состоять не менее чем из 8 символов, содержать как минимум одну строчную и одну прописную букву, хотя бы одну цифру и хотя бы один специальный символ.')

    def rep_password_reg(self):
        if not (self.data['password'] and zlib.crc32(self.ui.lineEdit_3.text().encode('utf-8')) == self.data['password']):
            self.data = ''
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.dial('Не корректные данные', 'Не верный пароль')
        else:
            self.check()

    def email_reg(self):
        if '@' in self.ui.lineEdit_4.text() and '@' not in [self.ui.lineEdit_4.text()[0], self.ui.lineEdit_4.text()[-1]]:
            self.data['email'] = self.ui.lineEdit_4.text()
            self.check()
        else:
            self.dial('Не корректные данные', 'Адрес электронной почты должен содержать ровно один символ @, но не начинаться с него и не заканчиваться им.')

    def phone_reg(self):
        phone = self.ui.lineEdit_5.text().replace(' ', '')
        if len(phone) == 11 and phone[0] == '8' and not (set(phone) - set(string.digits)) or len(phone) == 12 and phone[:2] == '+7' and not (set(phone[1:]) - set(string.digits)):
            self.data['phone'] = phone
            self.check()
        else:
            self.dial('Не корректные данные', 'Телефон вводится в следующем формате: сначала идёт +7 или 8, а затем 10 цифр с любым количеством пробелов ')

    def name_reg(self):
        self.data['name'] = self.ui.lineEdit_6.text()
        self.check()

    def city_reg(self):
        self.data['city'] = self.ui.lineEdit_7.text()
        self.check()

    def about_reg(self):
        self.data['about'] = self.ui.lineEdit_8.text()
        self.check()




app = QApplication(sys.argv)
w1 = Open()
w1.show()
app.exec()
