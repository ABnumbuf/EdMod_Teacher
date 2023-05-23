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
roles = ['Студент', 'Преподаватель']


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('EdMod Teacher')
        self.setFixedSize(650, 400)
        self.setFont(QFont('Arial', 12))
        self.main_layout = QGridLayout(self)
        self.setLayout(self.main_layout)

        self.current_win = 0
        self.role = ''
        self.user_name = ''

        self.w_lb_EdMod = QLabel("EdMod")
        self.w_lb_EdMod.setFont(QFont('Arial', 50))
        self.w_lb_EdMod.setAlignment(QtCore.Qt.AlignHCenter)
        self.w_lb_CryptMeth = QLabel("Криптографические методы")
        self.w_lb_CryptMeth.setAlignment(QtCore.Qt.AlignHCenter)
        self.w_lb_CryptMeth.setFixedHeight(110)

        self.w_lb_log_info = QLabel("Преподаватель")
        self.w_lb_log_msg = QLabel("")

        self.w_lb_username = QLabel("Имя:")
        self.inp_user_name = QLineEdit()
        self.w_lb_userpasw = QLabel("Пароль:")
        self.inp_user_pasw = QLineEdit()
        self.btn_log = QPushButton("Войти")
        self.btn_log.clicked.connect(self.click_btn_log)

        self.main_layout.addWidget(self.w_lb_log_info, 0, 0, 1, 3, QtCore.Qt.AlignRight)
        self.main_layout.addWidget(self.w_lb_EdMod, 1, 0, 1, 3, QtCore.Qt.AlignBottom)
        self.main_layout.addWidget(self.w_lb_CryptMeth, 2, 0, 1, 3, QtCore.Qt.AlignTop)
        self.main_layout.addWidget(self.w_lb_log_msg, 3, 0, 1, 3, QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(self.w_lb_username, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(self.inp_user_name, 4, 1, 1, 1)
        self.main_layout.addWidget(self.w_lb_userpasw, 5, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(self.inp_user_pasw, 5, 1, 1, 1)
        self.main_layout.addWidget(self.btn_log, 5, 2, 1, 1)


    def click_btn_reg(self):
        try:
            self.choosed_role = self.w_cmb_roles.currentText()
            self.user_name = self.inp_user_name.text().lower()
            self.user_pasw = self.inp_user_pasw.text()

            if self.user_name and self.user_pasw and self.choosed_role:
                if self.choosed_role == roles[0]: table = 'user'
                elif self.choosed_role == roles[1]: table = 'teacher'

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

                sql = f"SELECT {table}_name FROM {table}s where {table}_name='{self.user_name}'"
                cursor = self.connection.cursor()
                cursor.execute(sql)
                user = cursor.fetchall()

                if not user:
                    sql = f"insert into {table}s({table}_id, {table}_name, {table}_pasw) values(seq_{table}_id.nextval, :2, :3)"
                    print(sql)
                    with self.connection.cursor() as cursor:
                        cursor.execute(sql, [self.user_name, self.user_pasw])
                        print(f"Successfully created new user {self.user_name} in table {table}s: {datetime.datetime.now()}")
                    self.connection.commit()
                    self.w_lb_log_msg.setText(f'Пользователь создан')
                else: self.w_lb_log_msg.setText(f'Пользователь уже создан')
            else: self.w_lb_log_msg.setText(f'Введите значения')

            self.update()
        except ValueError:
            print(f"ERROR")
            return 0

    def click_btn_log(self):
        try:
            self.user_name = self.inp_user_name.text().lower()
            self.user_pasw = self.inp_user_pasw.text()

            self.w_lb_log_msg.setText('')

            if self.user_name and self.user_pasw:
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

                sql = f"SELECT teacher_name, teacher_pasw FROM TEACHERS where teacher_name='{self.user_name}'"
                
                cursor = self.connection.cursor()
                cursor.execute(sql)
                user = cursor.fetchall()

                if not user:
                    self.w_lb_log_msg.setText(f'Пользователь не найден')
                elif user[0][1] == self.user_pasw:
                    print(f"Successfully logged {self.user_name}: {datetime.datetime.now()}")

                    self.current_win = 1

                    self.w_lb_log_info.setParent(None)
                    self.w_lb_EdMod.setParent(None)
                    self.w_lb_CryptMeth.setParent(None)
                    self.w_lb_log_msg.setParent(None)
                    self.w_lb_username.setParent(None)
                    self.inp_user_name.setParent(None)
                    self.w_lb_userpasw.setParent(None)
                    self.inp_user_pasw.setParent(None)
                    self.btn_log.setParent(None)

                    self.w_lb_log_info.setText(f"Преподаватель - {self.user_name}")
                    
                    self.tab = QTabWidget(self)

                    self.page_educate = QWidget(self)
                    self.layout_educate = QGridLayout()
                    self.btn_back_educate = QPushButton("Назад")
                    self.btn_back_educate.clicked.connect(self.click_btn_back_educate)
                    self.w_lb_chs = QLabel("Выберите раздел")
                    self.w_lb_chs.setAlignment(QtCore.Qt.AlignHCenter)
                    self.w_cmb_mods = QComboBox()
                    self.w_cmb_mods.addItems(mods)
                    self.btn_next = QPushButton("Далее")
                    self.btn_next.clicked.connect(self.click_btn_next)
                    self.btn_back = QPushButton("Назад")
                    self.btn_back.clicked.connect(self.click_btn_back)

                    self.page_educate.setLayout(self.layout_educate)
                    self.layout_educate.addWidget(self.w_lb_log_info,    0, 0, 1, 3, QtCore.Qt.AlignRight)
                    self.layout_educate.addWidget(self.w_lb_EdMod,       1, 0, 1, 3, QtCore.Qt.AlignBottom)
                    self.layout_educate.addWidget(self.w_lb_CryptMeth,   2, 0, 1, 3, QtCore.Qt.AlignTop)
                    self.layout_educate.addWidget(self.w_lb_chs,         3, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.layout_educate.addWidget(self.w_cmb_mods,       4, 0, 1, 1)
                    self.layout_educate.addWidget(self.btn_next,         4, 1, 1, 1)
                    self.layout_educate.addWidget(self.btn_back_educate, 4, 2, 1, 1)

                    self.page_reg = QWidget(self)
                    self.layout_reg = QGridLayout()
                    self.page_reg.setLayout(self.layout_reg)

                    self.w_lb_log_info_2 = QLabel(f"Преподаватель - {self.user_name}")
                    self.w_lb_EdMod_2 = QLabel("EdMod")
                    self.w_lb_EdMod_2.setFont(QFont('Arial', 50))
                    self.w_lb_EdMod_2.setAlignment(QtCore.Qt.AlignHCenter)
                    self.w_lb_CryptMeth_2 = QLabel("Криптографические методы")
                    self.w_lb_CryptMeth_2.setAlignment(QtCore.Qt.AlignHCenter)
                    self.w_lb_CryptMeth_2.setFixedHeight(110)
                    self.w_lb_role = QLabel("Роль:")
                    self.w_lb_role.setAlignment(QtCore.Qt.AlignHCenter)
                    self.w_cmb_roles = QComboBox()
                    self.w_cmb_roles.addItems(roles)
                    self.btn_reg = QPushButton("Создать")
                    self.btn_reg.clicked.connect(self.click_btn_reg)

                    self.layout_reg.addWidget(self.w_lb_log_info_2,  0, 0, 1, 3, QtCore.Qt.AlignRight)
                    self.layout_reg.addWidget(self.w_lb_EdMod_2,     1, 0, 1, 3, QtCore.Qt.AlignBottom)
                    self.layout_reg.addWidget(self.w_lb_CryptMeth_2, 2, 0, 1, 3, QtCore.Qt.AlignTop)
                    self.layout_reg.addWidget(self.w_lb_log_msg,     3, 0, 1, 3, QtCore.Qt.AlignLeft)
                    self.layout_reg.addWidget(self.w_lb_role,        4, 0, 1, 1, QtCore.Qt.AlignLeft)
                    self.layout_reg.addWidget(self.w_cmb_roles,      4, 1, 1, 1)
                    self.layout_reg.addWidget(self.w_lb_username,    5, 0, 1, 1, QtCore.Qt.AlignLeft)
                    self.layout_reg.addWidget(self.inp_user_name,    5, 1, 1, 1)
                    self.layout_reg.addWidget(self.w_lb_userpasw,    6, 0, 1, 1, QtCore.Qt.AlignLeft)
                    self.layout_reg.addWidget(self.inp_user_pasw,    6, 1, 1, 1)
                    self.layout_reg.addWidget(self.btn_reg,          6, 2, 1, 1)

                    self.page_stat = QWidget(self)
                    self.layout_stat = QGridLayout()
                    self.page_stat.setLayout(self.layout_stat)

                    self.tab.addTab(self.page_educate, 'Обучение')
                    self.tab.addTab(self.page_reg,     'Регистрация пользователей')
                    self.tab.addTab(self.page_stat,    'Статистика')

                    self.main_layout.addWidget(self.btn_back, 0, 2, 1, 1, QtCore.Qt.AlignRight)
                    self.main_layout.addWidget(self.tab, 1, 0, 1, 3)

                else: self.w_lb_log_msg.setText(f'Неверный пароль')
            else: self.w_lb_log_msg.setText(f'Введите значения')
            self.update()
        except ValueError:
            print(f"ERROR")
            return 0
    
    
    def click_btn_next(self):
        try:
            choosed_mod = self.w_cmb_mods.currentText()
            print(f"Mod [{choosed_mod}] chosen {datetime.datetime.now()}")
            if choosed_mod in mods:

                self.current_win = 2
                self.w_cmb_mods.clear()
                self.w_lb_chs.setText(choosed_mod)
                if choosed_mod == mods[0]: self.w_cmb_mods.addItems(sub_1)
                elif choosed_mod == mods[1]: self.w_cmb_mods.addItems(sub_2)
                elif choosed_mod == mods[2]: self.w_cmb_mods.addItems(sub_3)
                elif choosed_mod == mods[3]:
                    mod_4.win_4(self, self.user_name)
                    self.w_cmb_mods.clear()
                    self.w_cmb_mods.addItems(mods)
            else:
                self.current_win = 1
                if   choosed_mod == sub_1[0]: mod_1_sub_1.win_1_1(self)
                elif choosed_mod == sub_1[1]: mod_1_sub_2.win_1_2(self)
                elif choosed_mod == sub_1[2]: mod_1_sub_3.win_1_3(self)
                elif choosed_mod == sub_2[0]: mod_2_sub_1.win_2_1(self)
                elif choosed_mod == sub_2[1]: mod_2_sub_2.win_2_2(self)
                elif choosed_mod == sub_2[2]: mod_2_sub_3.win_2_3(self)
                elif choosed_mod == sub_3[0]: mod_3_sub_1.win_3_1(self)
                elif choosed_mod == sub_3[1]: mod_3_sub_2.win_3_2(self)
                elif choosed_mod == sub_3[2]: mod_3_sub_3.win_3_3(self)
                self.w_cmb_mods.clear()
                self.w_cmb_mods.addItems(mods) 
                self.w_lb_chs.setText('Выбери раздел')

            self.update()
        except ValueError:
            print(f"ERROR")
            return 0
        
    def click_btn_back(self):
        try:
            if self.current_win == 1:
                self.current_win = 0

                self.w_lb_log_msg.setText('')
                self.w_lb_log_info.setText(f"Преподаватель")

                self.tab.setParent(None)
                self.btn_back.setParent(None)

                self.main_layout.addWidget(self.w_lb_log_info, 0, 0, 1, 3, QtCore.Qt.AlignRight)
                self.main_layout.addWidget(self.w_lb_EdMod, 1, 0, 1, 3, QtCore.Qt.AlignBottom)
                self.main_layout.addWidget(self.w_lb_CryptMeth, 2, 0, 1, 3, QtCore.Qt.AlignTop)
                self.main_layout.addWidget(self.w_lb_log_msg, 3, 0, 1, 3, QtCore.Qt.AlignLeft)
                self.main_layout.addWidget(self.w_lb_username, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
                self.main_layout.addWidget(self.inp_user_name, 4, 1, 1, 1)
                self.main_layout.addWidget(self.w_lb_userpasw, 5, 0, 1, 1, QtCore.Qt.AlignLeft)
                self.main_layout.addWidget(self.inp_user_pasw, 5, 1, 1, 1)
                self.main_layout.addWidget(self.btn_log, 5, 2, 1, 1)
            self.update()
        except ValueError:
            print(f"ERROR")
            return 0

    def click_btn_back_educate(self):
        try:
            self.w_cmb_mods.clear()
            self.w_cmb_mods.addItems(mods)
            self.w_lb_chs.setText('Выбери раздел')
            
            
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
