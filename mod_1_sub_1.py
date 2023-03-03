# This Python file uses the following encoding: windows-1251

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from util import read_text, get_random_message
import My_ElGamal as elg

def get_task_val():
    v_tsk_p = elg.get_prime_number_in_range(10, 100)
    v_tsk_g = elg.get_primitive_root(v_tsk_p)
    v_tsk_x = elg.get_prime_number_in_range(1, v_tsk_p - 1)
    v_tsk_m = get_random_message(6)
    return v_tsk_p,v_tsk_g,v_tsk_x,v_tsk_m


class Window_1_1(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('ЭЦП по схеме Эль-Гамаля: Генерация ключей')
        self.setFixedSize(700, 800)
        # self.setStyleSheet('background-color: #333232; color: #FFFFEB;')
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        tab = QTabWidget(self)
        tab.setFont(QFont('Arial', 12))
        # Page Theory
        page_text = QWidget(self)
        layout = QFormLayout()
        page_text.setLayout(layout)
        text = read_text('text_mod1_block1.html')
        label_text = QLabel(text)
        label_text.setFont(QFont('Arial', 12))
        label_text.setWordWrap(True)
        scrollArea = QScrollArea()
        scrollArea.setWidget(label_text)
        layout.addRow(scrollArea)
        # Page Example
        page_example = QWidget(self)
        page_example.setFont(QFont('Arial', 12))
        layout_ex = QGridLayout()
        page_example.setLayout(layout_ex)
        tab_ex = QTabWidget(self)
        tab_ex.setTabPosition(QTabWidget.East)

        page_ex_1 = QWidget(self)

        layout_ex_1 = QGridLayout()
        page_ex_1.setLayout(layout_ex_1)
        layout_ex_1.addWidget(QLabel('Нахождение простых чисел в диапазоне значений'),0,0,1,3)
        layout_ex_1.addWidget(QLabel('Введи диапазон значений:'),1,0)
        self.inp_ex_lb = QLineEdit()
        self.inp_ex_rb = QLineEdit()
        btn_ex_1 = QPushButton("Решить")
        # btn_ex_1.clicked.connect(self.click_btn_ex)
        self.outp_ex_1 = QTextBrowser()
        layout_ex_1.addWidget(self.inp_ex_lb,1,1)
        layout_ex_1.addWidget(self.inp_ex_rb,1,2)
        layout_ex_1.addWidget(btn_ex_1,2,0,1,3)
        layout_ex_1.addWidget(QLabel('Результат:'),3,0,1,3)
        layout_ex_1.addWidget(self.outp_ex_1,4,0,1,3)

        page_ex_2 = QWidget(self)

        layout_ex_2 = QGridLayout()
        page_ex_2.setLayout(layout_ex_2)
        layout_ex_2.addWidget(QLabel('Нахождение первообразных корней числа'),0,0,1,3)
        layout_ex_2.addWidget(QLabel('Введи число:'),1,0)
        self.inp_ex_root = QLineEdit()
        btn_ex_2 = QPushButton("Решить")
        # btn_ex_2.clicked.connect(self.click_btn_ex)
        self.outp_ex_2 = QTextBrowser()
        layout_ex_2.addWidget(self.inp_ex_root,1,1)
        layout_ex_2.addWidget(btn_ex_2,2,0,1,3)
        layout_ex_2.addWidget(QLabel('Результат:'),3,0,1,3)
        layout_ex_2.addWidget(self.outp_ex_2,4,0,1,3)

        page_ex_3 = QWidget(self)

        layout_ex_3 = QGridLayout()
        page_ex_3.setLayout(layout_ex_3)
        layout_ex_3.addWidget(QLabel(\
            '<p>Нахождение y &#8801; g<sup>x</sup> (mod p)</p>')\
            ,0,0,1,2)
        layout_ex_3.addWidget(QLabel('Введи значения:'),1,0,1,2)
        self.inp_ex_g = QLineEdit()
        self.inp_ex_x = QLineEdit()
        self.inp_ex_p = QLineEdit()
        btn_ex_3 = QPushButton("Решить")
        # btn_ex_3.clicked.connect(self.click_btn_ex)
        self.outp_ex_3 = QTextBrowser()
        layout_ex_3.addWidget(QLabel('g = '),2,0)
        layout_ex_3.addWidget(QLabel('x = '),3,0)
        layout_ex_3.addWidget(QLabel('p = '),4,0)
        layout_ex_3.addWidget(self.inp_ex_g,2,1)
        layout_ex_3.addWidget(self.inp_ex_x,3,1)
        layout_ex_3.addWidget(self.inp_ex_p,4,1)
        layout_ex_3.addWidget(btn_ex_3,5,0,1,2)
        layout_ex_3.addWidget(QLabel('Результат:'),6,0,1,2)
        layout_ex_3.addWidget(self.outp_ex_3,7,0,1,2)

        tab_ex.addTab(page_ex_1, '1')
        tab_ex.addTab(page_ex_2, '2')
        tab_ex.addTab(page_ex_3, '3')
        layout_ex.addWidget(tab_ex, 0, 0, 2, 1)

        # Page Task
        page_task = QWidget(self)
        page_task.setFont(QFont('Arial', 12))
        layout_tsk = QGridLayout()
        page_task.setLayout(layout_tsk)
        tab_tsk = QTabWidget(self)
        tab_tsk.setTabPosition(QTabWidget.East)

        page_tsk_1 = QWidget(self)

        layout_tsk_1 = QGridLayout()
        page_tsk_1.setLayout(layout_tsk_1)
        layout_tsk_1.addWidget(QLabel('Нахождение простых чисел в диапазоне значений'),0,0,1,3)
        layout_tsk_1.addWidget(QLabel('Введи диапазон значений:'),1,0)
        self.inp_tsk_lb = QLineEdit()
        self.inp_tsk_rb = QLineEdit()
        btn_tsk_1_chk = QPushButton("Решить")
        # btn_tsk_1_chk.clicked.connect(self.click_btn_tsk_1_chk)
        self.outp_tsk_1 = QTextBrowser()
        layout_tsk_1.addWidget(self.inp_tsk_lb,1,1)
        layout_tsk_1.addWidget(self.inp_tsk_rb,1,2)
        layout_tsk_1.addWidget(btn_tsk_1_chk,2,0,1,3)
        layout_tsk_1.addWidget(QLabel('Результат:'),3,0,1,3)
        layout_tsk_1.addWidget(self.outp_tsk_1,4,0,1,3)

        page_tsk_2 = QWidget(self)

        layout_tsk_2 = QGridLayout()
        page_tsk_2.setLayout(layout_tsk_2)
        layout_tsk_2.addWidget(QLabel('Нахождение первообразных корней числа'),0,0,1,3)
        layout_tsk_2.addWidget(QLabel('Введи число:'),1,0)
        self.inp_tsk_root = QLineEdit()
        btn_tsk_2_chk = QPushButton("Решить")
        # btn_tsk_2_chk.clicked.connect(self.click_btn_tsk_2_chk)
        self.outp_tsk_2 = QTextBrowser()
        layout_tsk_2.addWidget(self.inp_tsk_root,1,1)
        layout_tsk_2.addWidget(btn_tsk_2_chk,2,0,1,3)
        layout_tsk_2.addWidget(QLabel('Результат:'),3,0,1,3)
        layout_tsk_2.addWidget(self.outp_tsk_2,4,0,1,3)

        page_tsk_3 = QWidget(self)

        layout_tsk_3 = QGridLayout()
        page_tsk_3.setLayout(layout_tsk_3)
        layout_tsk_3.addWidget(QLabel(\
            '<p>Нахождение y &#8801; g<sup>x</sup> (mod p)</p>')\
            ,0,0,1,2)
        layout_tsk_3.addWidget(QLabel('Введи ответ: y = '),2,0)
        self.inp_tsk_y = QLineEdit()
        btn_tsk_3_chk = QPushButton("Решить")
        # btn_tsk_3_chk.clicked.connect(self.click_btn_tsk_2_chk)
        btn_tsk_3_rst = QPushButton("Обновить")
        # btn_tsk_3_rst.clicked.connect(self.click_btn_tsk_2_rst)
        self.outp_tsk_3 = QTextBrowser()
        layout_tsk_3.addWidget(self.inp_tsk_y,2,1)
        layout_tsk_3.addWidget(btn_tsk_3_chk,3,0)
        layout_tsk_3.addWidget(btn_tsk_3_rst,3,1)
        layout_tsk_3.addWidget(QLabel('Результат:'),4,0,1,2)
        layout_tsk_3.addWidget(self.outp_tsk_3,5,0,1,2)

        tab_tsk.addTab(page_tsk_1, '1')
        tab_tsk.addTab(page_tsk_2, '2')
        tab_tsk.addTab(page_tsk_3, '3')
        layout_tsk.addWidget(tab_tsk, 0, 0, 2, 1)

        tab.addTab(page_text, 'Теория')
        tab.addTab(page_example, 'Примеры')
        tab.addTab(page_task, 'Задачи')
        
        main_layout.addWidget(tab, 0, 0, 2, 1)


    def click_btn_ex(self):
        try:
            v_exmpl_m = str(self.inp_ex_m.text())
            v_exmpl_p = int(self.inp_ex_p.text())
            v_exmpl_g = int(self.inp_ex_g.text())
            v_exmpl_x = int(self.inp_ex_x.text())
            self.outp_ex.setText(elg.ds_ElGamal_outp(v_exmpl_m, v_exmpl_p, v_exmpl_g, v_exmpl_x))
        except ValueError:
            self.outp_ex.setText(f"Введи значения: \nm - строка \np, g, x - целые числa")
    
    def click_btn_tsk_chk(self):
        try:
            v_tsk_r = int(self.tsk_r.text())
            v_tsk_s = int(self.tsk_s.text())
            v_r, v_s = elg.ds_ElGamal(self.v_tsk_m, self.v_tsk_p, self.v_tsk_g, self.v_tsk_x)
            if (v_tsk_r == v_r and v_tsk_s == v_s):
                self.outp_tsk.setText(f"r = {v_tsk_r}\ns = {v_tsk_s}\nВерно")
            else:
                self.outp_tsk.setText(f"r = {v_tsk_r}\ns = {v_tsk_s}\nНеверно")
            self.update()
        except ValueError:
            self.outp_tsk.setText(f"Введи значения: \nr - целое число \ns - целое число")

    def click_btn_tsk_rst(self):
        try:
            self.v_tsk_p, self.v_tsk_g, self.v_tsk_x, self.v_tsk_m = get_task_val()
            self.task_text.setText(
                f'Являеется ли подпись правильной для: \np = {self.v_tsk_p}, g = {self.v_tsk_g}, x = {self.v_tsk_x}, m = {self.v_tsk_m}')
            self.update()
        except ValueError:
            print(ValueError)


def win_1_1(w):

    w.window = Window_1_1()
    w.window.show()
