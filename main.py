# This Python file uses the following encoding: windows-1251

import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui
import mod_1_sub_1, mod_1_sub_2, mod_1_sub_3 \
    , mod_2_sub_1 , mod_2_sub_2, mod_2_sub_3 \
    , mod_3_sub_1, mod_3_sub_2, mod_3_sub_3 \
    , mod_4
import oracledb
import datetime

mods = ['ЭЦП по схеме Эль-Гамаля'
        ,'Задача дискретного логарифмирования'
        ,'Рюкзачная криптосистема'
        , 'Тестирование']
sub_1 = ['Генерация ключей'
        ,'Создание подписи'
        ,'Валидация подписи']
sub_2 = ['Метод согласования'
        ,'Метод СПХ'
        ,'Время выполнения']
sub_3 = ['Задача о рюкзаке'
        ,'Алгоритм шифрования'
        ,'Алгоритм дешифрования']


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('EdMod')
        self.setFixedSize(650, 250)
        self.setFont(QFont('Arial', 12))
        self.main_layout = QGridLayout(self)
        self.setLayout(self.main_layout)
        w_lb_EdMod = QLabel("EdMod")
        w_lb_EdMod.setFont(QFont('Arial', 50))
        w_lb_EdMod.setAlignment(QtCore.Qt.AlignHCenter)
        w_lb_EdMod.setFixedHeight(60)
        w_lb_CryptMeth = QLabel("Криптографические методы")
        w_lb_CryptMeth.setAlignment(QtCore.Qt.AlignHCenter)
        w_lb_CryptMeth.setFixedHeight(110)
        self.w_lb_user = QLabel("")
        self.w_lb_user.setFixedHeight(20)
        self.w_lb_user.setAlignment(QtCore.Qt.AlignRight)
        self.w_lb_log_info = QLabel("")
        self.w_lb_username = QLabel("Введите имя:")
        self.inp_user_name = QLineEdit()
        self.w_lb_userpasw = QLabel("Введите пароль:")
        self.inp_user_pasw = QLineEdit()
        self.btn_log = QPushButton("Войти")
        self.btn_log.clicked.connect(self.click_btn_log)
        self.btn_reg = QPushButton("Создать")
        self.btn_reg.clicked.connect(self.click_btn_reg)
        self.w_lb_chs = QLabel("Выберите раздел")
        self.w_lb_chs.setAlignment(QtCore.Qt.AlignHCenter)
        self.cmb = QComboBox()
        self.cmb.addItems(mods)
        self.btn = QPushButton("Далее")
        self.btn.clicked.connect(self.click_btn)

        self.main_layout.addWidget(self.w_lb_user, 0, 0, 1, 3, QtCore.Qt.AlignBottom)
        self.main_layout.addWidget(w_lb_EdMod, 1, 0, 1, 3, QtCore.Qt.AlignBottom)
        self.main_layout.addWidget(w_lb_CryptMeth, 2, 0, 1, 3, QtCore.Qt.AlignBottom)
        self.main_layout.addWidget(self.w_lb_log_info, 3, 0, 1, 3, QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(self.w_lb_username, 4, 0)
        self.main_layout.addWidget(self.inp_user_name, 4, 1, QtCore.Qt.AlignBottom)
        self.main_layout.addWidget(self.btn_reg, 4, 2, QtCore.Qt.AlignBottom)
        self.main_layout.addWidget(self.w_lb_userpasw, 5, 0)
        self.main_layout.addWidget(self.inp_user_pasw, 5, 1, QtCore.Qt.AlignBottom)
        self.main_layout.addWidget(self.btn_log, 5, 2, QtCore.Qt.AlignBottom)
        try:

            oracledb.init_oracle_client()

            self.connection = oracledb.connect(
                user="edmod",
                password="edmod",
                host="192.168.92.60",
                port="49161",
                service_name="xe")

            if self.connection: print(f"Successfully connected to Database: {datetime.datetime.now()}")
            else: print(f"Error with connect to Database: {datetime.datetime.now()}")
        except ValueError:
            print(f"ERROR")
            return 0
        

    def click_btn_reg(self):
        try:
            self.user_name = self.inp_user_name.text().lower()
            user_pasw = self.inp_user_pasw.text()
            if self.user_name and user_pasw:

                sql = f"SELECT user_name FROM USERS where user_name='{self.user_name}'"
                cursor = self.connection.cursor()
                cursor.execute(sql)
                user = cursor.fetchall()

                if not user:

                    sql = f"insert into users(user_id, user_name, user_pasw) values(seq_user_id.nextval, :2, :3)"
                    with self.connection.cursor() as cursor:
                        cursor.execute(sql, [self.user_name, user_pasw])
                        print(f"Successfully created new user {self.user_name}: {datetime.datetime.now()}")
                    self.connection.commit()
                    print(f"Successfully logged {self.user_name}: {datetime.datetime.now()}")
                    self.w_lb_log_info.setParent(None)
                    self.w_lb_username.setParent(None)
                    self.inp_user_name.setParent(None)
                    self.btn_reg.setParent(None)
                    self.w_lb_userpasw.setParent(None)
                    self.inp_user_pasw.setParent(None)
                    self.btn_log.setParent(None)
                    self.main_layout.addWidget(self.w_lb_chs, 2, 0, 1, 3, QtCore.Qt.AlignBottom)
                    self.main_layout.addWidget(self.cmb, 3, 0, 1, 2, QtCore.Qt.AlignBottom)
                    self.main_layout.addWidget(self.btn, 3, 2, QtCore.Qt.AlignBottom)
                    self.w_lb_user.setText(self.user_name)
                else:
                    self.w_lb_log_info.setText(f'Пользователь уже создан')
            else:
                self.w_lb_log_info.setText(f'Введите значения')
            self.update()
        except ValueError:
            print(f"ERROR")
            return 0

    def click_btn_log(self):
        try:
            self.user_name = self.inp_user_name.text().lower()
            user_pasw = self.inp_user_pasw.text()
            if self.user_name and user_pasw:

                sql = f"SELECT user_name, user_pasw FROM USERS where user_name='{self.user_name}'"
                cursor = self.connection.cursor()
                cursor.execute(sql)
                user = cursor.fetchall()

                if not user:
                    self.w_lb_log_info.setText(f'Пользователь не найден')
                elif user[0][1] == user_pasw:
                    print(f"Successfully logged {self.user_name}: {datetime.datetime.now()}")
                    self.w_lb_log_info.setParent(None)
                    self.w_lb_username.setParent(None)
                    self.inp_user_name.setParent(None)
                    self.btn_reg.setParent(None)
                    self.w_lb_userpasw.setParent(None)
                    self.inp_user_pasw.setParent(None)
                    self.btn_log.setParent(None)
                    self.main_layout.addWidget(self.w_lb_chs, 2, 0, 1, 3, QtCore.Qt.AlignBottom)
                    self.main_layout.addWidget(self.cmb, 3, 0, 1, 2, QtCore.Qt.AlignBottom)
                    self.main_layout.addWidget(self.btn, 3, 2, QtCore.Qt.AlignBottom)
                    self.w_lb_user.setText(self.user_name)
                else:
                    self.w_lb_log_info.setText(f'Неверный пароль')
            else:
                self.w_lb_log_info.setText(f'Введите значения')
            self.update()

        except ValueError:
            print(f"ERROR")
            return 0
    
    
    def click_btn(self):
        try:
            choosed = self.cmb.currentText()
            print(choosed)
            if choosed in mods:
                self.cmb.clear()
                self.btn.setText('Начать')
                self.w_lb_chs.setText(f'Выберите подраздел [{choosed}]')
                if choosed == mods[0]: self.cmb.addItems(sub_1)
                elif choosed == mods[1]: self.cmb.addItems(sub_2)
                elif choosed == mods[2]: self.cmb.addItems(sub_3)
                elif choosed == mods[3]:
                    mod_4.win_4(self, self.user_name)
                    self.cmb.clear()
                    self.cmb.addItems(mods)
                    self.btn.setText('Далее')
                    self.w_lb_chs.setText(f'Выберите раздел')
                    self.update()
                
            else:
                if   choosed == sub_1[0]: mod_1_sub_1.win_1_1(self)
                elif choosed == sub_1[1]: mod_1_sub_2.win_1_2(self)
                elif choosed == sub_1[2]: mod_1_sub_3.win_1_3(self)
                elif choosed == sub_2[0]: mod_2_sub_1.win_2_1(self)
                elif choosed == sub_2[1]: mod_2_sub_2.win_2_2(self)
                elif choosed == sub_2[2]: mod_2_sub_3.win_2_3(self)
                elif choosed == sub_3[0]: mod_3_sub_1.win_3_1(self)
                elif choosed == sub_3[1]: mod_3_sub_2.win_3_2(self)
                elif choosed == sub_3[2]: mod_3_sub_3.win_3_3(self)
                self.cmb.clear()
                self.cmb.addItems(mods)
                self.btn.setText('Далее')
                self.w_lb_chs.setText(f'Выберите раздел')
            self.update()
        except ValueError:
            print(f"ERROR")
            return 0


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyle('Fusion')

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
