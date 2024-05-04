from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
import sys, os, json, string, zlib
from register.Open import Ui_MainWindow
from plan5.register.Register import Ui_Form
import plan5.register.plan4 as plan


class Open(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.w = None

        if not os.path.join(os.getcwd(), 'people.json'):
            with open(os.path.join(os.getcwd(), 'people.json'), 'w') as file:
                json.dump([{'login': 'gleb', 'password': '123'}], file)

        self.ui.pushButton_2.clicked.connect(self.pressed)
        self.ui.pushButton.clicked.connect(self.regist)

    def pressed(self):
        with open(os.path.join(os.getcwd(), 'people.json'), encoding='utf-8') as file:
            self.data = json.load(file)
            person0 = None
            for person in self.data:
                if person['login'] == self.ui.lineEdit.text() and person['password'] == zlib.crc32(self.ui.lineEdit_2.text().encode('utf-8')):
                    person0 = person
            if self.data and person0 is not None:
                self.good = plan.Question(person0['login'])
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
        self.ui.pushButton.clicked.connect(self.register)

    def check(self):
        if all(self.data[key] for key in self.data):
            with open(os.path.join(os.getcwd(), 'people.json')) as file:
                lis = json.load(file)
                lis.append(self.data)
            with open(os.path.join(os.getcwd(), 'people.json'), 'w') as file1:
                json.dump(lis, file1, indent=2)

            self.good = plan.Question(self.data['login'])
            self.good.show()
            self.close()

    def dial(self, title, mistake):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(title)
        dlg.setText(mistake)
        dlg.setIcon(QMessageBox.Icon.NoIcon)
        dlg.exec()

    def login_reg(self):
        if len(self.ui.lineEdit.text()) >= 5 and not set(self.ui.lineEdit.text()) - (
                set(string.ascii_letters) | set(string.digits)):
            self.data['login'] = self.ui.lineEdit.text()
        else:
            self.dial('Не корректные данные',
                    'Логин состоит не менее чем из 5 символов из набора латинских букв и цифр')
            self.ui.lineEdit.clear()
    def password_reg(self):
        if len(self.ui.lineEdit_2.text()) >= 8 and all(set(self.ui.lineEdit_2.text()) & set(i) for i in
                                                       [string.ascii_uppercase, string.ascii_lowercase, string.digits,
                                                        string.punctuation]):
            self.data['password'] = zlib.crc32(self.ui.lineEdit_2.text().encode('utf-8'))
        else:
            self.dial('Не корректные данные',
                      'Пароль должен состоять не менее чем из 8 символов, содержать как минимум одну строчную и одну прописную букву, хотя бы одну цифру и хотя бы один специальный символ.')
            self.ui.lineEdit_2.clear()
    def rep_password_reg(self):
        if not (self.data['password'] and zlib.crc32(self.ui.lineEdit_3.text().encode('utf-8')) == self.data['password']):
            self.data['password'] = ''
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.dial('Не корректные данные', 'Не верный пароль')

    def email_reg(self):
        if '@' in self.ui.lineEdit_4.text() and '@' not in [self.ui.lineEdit_4.text()[0],
                                                            self.ui.lineEdit_4.text()[-1]]:
            self.data['email'] = self.ui.lineEdit_4.text()
        else:
            self.dial('Не корректные данные',
                      'Адрес электронной почты должен содержать ровно один символ @, но не начинаться с него и не заканчиваться им.')
            self.ui.lineEdit_4.clear()
    def phone_reg(self):
        phone = self.ui.lineEdit_5.text().replace(' ', '')
        if len(phone) == 11 and phone[0] == '8' and not (set(phone) - set(string.digits)) or len(phone) == 12 and phone[
                                                                                                                  :2] == '+7' and not (
                set(phone[1:]) - set(string.digits)):
            self.data['phone'] = phone
        else:
            self.dial('Не корректные данные',
                      'Телефон вводится в следующем формате: сначала идёт +7 или 8, а затем 10 цифр с любым количеством пробелов ')
            self.ui.lineEdit_5.clear()
    def name_reg(self):
        self.data['name'] = self.ui.lineEdit_6.text()

    def city_reg(self):
        self.data['city'] = self.ui.lineEdit_7.text()

    def about_reg(self):
        self.data['about'] = self.ui.lineEdit_8.text()

    def register(self):
        self.login_reg()
        self.password_reg()
        self.rep_password_reg()
        self.email_reg()
        self.phone_reg()
        self.name_reg()
        self.city_reg()
        self.about_reg()
        self.check()


app = QApplication(sys.argv)
w1 = Open()
w1.show()
app.exec()

