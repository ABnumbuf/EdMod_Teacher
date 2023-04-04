# This Python file uses the following encoding: windows-1251

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
import My_Knapsack as ks
from util import read_text, get_random_message, extended_gcd
import random
import sys
import PyQt5





class Window_4(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Тестирование')
        self.setFixedSize(1000, 800)
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        self.w_chb_1_1 = QCheckBox("Генерация ключей")
        self.w_chb_1_2 = QCheckBox("Создание подписи")
        self.w_chb_1_3 = QCheckBox("Проверка подписи")
        self.w_chb_2_1 = QCheckBox("Метод согласования")
        self.w_chb_2_2= QCheckBox("Метод Сильвестра-Полига-Хеллмана")
        self.w_chb_3_1 = QCheckBox("Задача о рюкзаке")
        self.w_chb_3_2 = QCheckBox("Алгоритм шифрования")
        self.w_chb_3_3 = QCheckBox("Алгоритм дешифрования")
        self.w_bt_strt = QPushButton("Начать")
        self.w_bt_strt.clicked.connect(self.click_btn_strt)
        self.w_bt_fnsh = QPushButton("Завершить")
        # self.w_bt_cln = QPushButton("Очистить")
        # self.w_bt_cln.clicked.connect(self.click_btn_cln)
        self.w_outp_stat = QTextBrowser()
        self.w_scrollArea = QScrollArea()
        self.inp_1 = QLineEdit()
        self.inp_2 = QLineEdit()
        self.inp_3 = QLineEdit()
        self.inp_4 = QLineEdit()
        self.inp_5 = QLineEdit()
        self.inp_6 = QLineEdit()
        self.inp_7 = QLineEdit()
        self.inp_8 = QLineEdit()
        self.list_inp = [self.inp_1, 
                    self.inp_2,
                    self.inp_3,
                    self.inp_4,
                    self.inp_5,
                    self.inp_6,
                    self.inp_7,
                    self.inp_8]
         
        
        main_layout.addWidget(self.w_scrollArea,                               0, 0, 17, 1)
        main_layout.addWidget(QLabel("ЭЦП по схеме Эль-Гамаля"),             1, 1, 1, 1)
        main_layout.addWidget(self.w_chb_1_1,                                2, 1, 1, 1)
        main_layout.addWidget(self.w_chb_1_2,                                3, 1, 1, 1)
        main_layout.addWidget(self.w_chb_1_3,                                4, 1, 1, 1)
        main_layout.addWidget(QLabel("Задача дискретного логарифмирования"), 5, 1, 1, 1)
        main_layout.addWidget(self.w_chb_2_1,                                6, 1, 1, 1)
        main_layout.addWidget(self.w_chb_2_2,                                7, 1, 1, 1)
        main_layout.addWidget(QLabel("Рюкзачная криптосистема"),             8, 1, 1, 1)
        main_layout.addWidget(self.w_chb_3_1,                                9, 1, 1, 1)
        main_layout.addWidget(self.w_chb_3_2,                               10, 1, 1, 1)
        main_layout.addWidget(self.w_chb_3_3,                               12, 1, 1, 1)
        main_layout.addWidget(self.w_bt_strt,                               13, 1, 1, 1)
        main_layout.addWidget(self.w_bt_fnsh,                               14, 1, 1, 1)
        # main_layout.addWidget(self.w_bt_cln,                                15, 1, 1, 1)
        main_layout.addWidget(self.w_outp_stat,                             16, 1, 1, 1)


    def click_btn_strt(self):
        try:
            list_mod = ['Генерация ключей'
                        ,'Создание подписи'
                        ,'Валидация подписи'
                        , 'Метод согласования'
                        ,'Метод СПХ'
                        ,'Задача о рюкзаке'
                        ,'Алгоритм шифрования'
                        ,'Алгоритм дешифрования']
            self.w_w_scroll = QWidget()
            self.w_box_tst = QVBoxLayout()
            test_plan = [self.w_chb_1_1.isChecked(),
                         self.w_chb_1_2.isChecked(),
                         self.w_chb_1_3.isChecked(),
                         self.w_chb_2_1.isChecked(),
                         self.w_chb_2_2.isChecked(),
                         self.w_chb_3_1.isChecked(),
                         self.w_chb_3_2.isChecked(),
                         self.w_chb_3_3.isChecked()]
            count = 0
            for i in range(len(test_plan)):
                if test_plan[i]:
                    self.w_box_tst.addWidget(QLabel(f"Задача {count+1}"))
                    self.w_box_tst.addWidget(QLabel(f"{list_mod[i]}"))
                    self.w_box_tst.addWidget(self.list_inp[i])
                    count +=1
            self.w_w_scroll.setLayout(self.w_box_tst)
            self.w_scrollArea.setWidget(self.w_w_scroll)
            self.w_outp_stat.setText(str(test_plan))
            self.update()
        except ValueError:
            self.w_outp_stat.setText(f"Выбери темы для тестирования")
            self.update()
    
    # def click_btn_cln(self):
    #     try:
    #         self.w_w_scroll = QWidget()
    #         self.w_box_tst = QVBoxLayout()
    #         self.w_w_scroll.setLayout(self.w_box_tst)
    #         self.w_scrollArea.setWidget(self.w_w_scroll)
    #         self.w_outp_stat.setText(f"")
    #         self.update()
    #     except ValueError:
    #         self.w_outp_stat.setText(f"")
    #         self.update()



def win_4():
    app = QApplication(sys.argv)
    
    window = Window_4()
    window.show()
    app.exec()

win_4()