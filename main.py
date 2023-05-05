# This Python file uses the following encoding: windows-1251

import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui
import mod_1_sub_1, mod_1_sub_2, mod_1_sub_3 \
    , mod_2_sub_1 , mod_2_sub_2, mod_2_sub_3 \
    , mod_3_sub_1, mod_3_sub_2, mod_3_sub_3 \
    , mod_4

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
        lb1 = QLabel("EdMod")
        # lb1.setStyleSheet('color: #FFCB69')
        lb2 = QLabel("Криптографические методы")

        self.lb6 = QLabel("")
        self.lb4 = QLabel("Введите имя:")
        self.inp_user_name = QLineEdit()
        self.lb5 = QLabel("Введите пароль:")
        self.inp_user_pasw = QLineEdit()
        self.btn_log = QPushButton("Далее")
        self.btn_log.clicked.connect(self.click_btn_log)

        self.lb3 = QLabel("Выберите раздел")
        lb1.setFont(QFont('Arial', 50))
        lb1.setAlignment(QtCore.Qt.AlignHCenter)
        lb2.setAlignment(QtCore.Qt.AlignHCenter)
        self.lb3.setAlignment(QtCore.Qt.AlignHCenter)
        lb2.setFixedHeight(125)
        self.cmb = QComboBox()
        self.cmb.addItems(mods)
        self.btn = QPushButton("Далее")
        self.btn.clicked.connect(self.click_btn)
        self.btn.setFixedSize(100, 26)
        self.main_layout.addWidget(lb1, 0, 0, 1, 3)
        self.main_layout.addWidget(lb2, 1, 0, 1, 3)

        self.main_layout.addWidget(self.lb6, 2, 0)
        self.main_layout.addWidget(self.lb4, 3, 0)
        self.main_layout.addWidget(self.inp_user_name, 3, 1, QtCore.Qt.AlignBottom)
        self.main_layout.addWidget(self.lb5, 4, 0)
        self.main_layout.addWidget(self.inp_user_pasw, 4, 1, QtCore.Qt.AlignBottom)
        self.main_layout.addWidget(self.btn_log, 4, 2, QtCore.Qt.AlignBottom)


    def click_btn_log(self):
        try:
            user_name = self.inp_user_name.text()
            user_pasw = self.inp_user_pasw.text()
            if user_name and user_pasw:

                import oracledb
                import datetime

                oracledb.init_oracle_client()

                connection = oracledb.connect(
                    user="edmod",
                    password="edmod",
                    host="192.168.92.60",
                    port="49161",
                    service_name="xe")

                if connection: print(f"Successfully connected to Database: {datetime.datetime.now()}")

                sql = f"SELECT user_name, user_pasw FROM USERS where user_name='{user_name}'"
                cursor = connection.cursor()
                cursor.execute(sql)
                user = cursor.fetchall()

                if not user:
                    sql = f"insert into users(user_id, user_name) values(:1, :2)"
                    with connection.cursor() as cursor:
                        cursor.execute(sql, [0, user_name])
                        print(f"Successfully created new user {user_name}: {datetime.datetime.now()}")
                    connection.commit()
                elif user[0][1]==user_pasw:
                    print(f"Successfully logged {user_name}: {datetime.datetime.now()}")
                    self.lb4.setParent(None)
                    self.inp_user_name.setParent(None)
                    self.lb5.setParent(None)
                    self.inp_user_pasw.setParent(None)
                    self.btn_log.setParent(None)
                    self.main_layout.addWidget(self.lb3, 2, 0, 1, 3, QtCore.Qt.AlignBottom)
                    self.main_layout.addWidget(self.cmb, 3, 0, 1, 2, QtCore.Qt.AlignBottom)
                    self.main_layout.addWidget(self.btn, 3, 2, QtCore.Qt.AlignBottom)
                else:
                    self.lb6.setText(f'Неверный пароль')
            self.lb6.setText(f'Введите значения')
            self.update()



        except ValueError:
            print(f"ERROR")
    
    
    def click_btn(self):
        try:
            choosed = self.cmb.currentText()
            print(choosed)
            if choosed in mods:
                self.cmb.clear()
                self.btn.setText('Начать')
                self.lb3.setText(f'Выбери подраздел [{choosed}]')
                if choosed == mods[0]: self.cmb.addItems(sub_1)
                elif choosed == mods[1]: self.cmb.addItems(sub_2)
                elif choosed == mods[2]: self.cmb.addItems(sub_3)
                elif choosed == mods[3]:
                    mod_4.win_4(self)
                    self.cmb.clear()
                    self.cmb.addItems(mods)
                    self.btn.setText('Далее')
                    self.lb3.setText(f'Выбери раздел')
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
                self.lb3.setText(f'Выбери раздел')
            self.update()
        except ValueError:
            print(f"ERROR")
    



    


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyle('Fusion')

    dark_palette = QtGui.QPalette()
    dark_palette.setColor(QtGui.QPalette.Background, QtGui.QColor(255, 241, 214))
    dark_palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(86, 69, 57))
    dark_palette.setColor(QtGui.QPalette.BrightText, QtGui.QColor(208, 140, 96))
    dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(255, 235, 194))
    dark_palette.setColor(QtGui.QPalette.Text, QtGui.QColor(86, 69, 57))
    dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(255, 203, 105))
    dark_palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(86, 69, 57))
    dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(255, 203, 105))
    dark_palette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(86, 69, 57))

    #app.setPalette(dark_palette)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
