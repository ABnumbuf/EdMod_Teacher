# This Python file uses the following encoding: windows-1251

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
import My_Knapsack as ks
from util import read_text, get_random_message
import random


def get_task_val():
    v_tsk_v = [x ** random.randint(1,3) for x in range(2,random.randint(5,6))]
    v_tsk_v.sort()
    v_tsk_m = random.randint(2, 90)
    v_tsk_w = random.randint(2, 40)
    while random.extended_gcd(v_tsk_m,v_tsk_w)[0] == 1:
        v_tsk_m = random.randint(2, 90)
        v_tsk_w = random.randint(2, 40)
    v_tsk_text = get_random_message(6)
    return v_tsk_v, v_tsk_m, v_tsk_w, v_tsk_text.upper()


class Window_3_3(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Рюкзачная криптосистема: Алгоритм шифрования')
        self.setFixedSize(700, 800)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        tab = QTabWidget(self)
        tab.setFont(QFont('Arial', 14))
        # Page Theory
        page_text = QWidget(self)
        layout = QFormLayout()
        page_text.setLayout(layout)
        text = read_text('text_mod2_block2.html')
        label_text = QLabel(text)
        label_text.setFont(QFont('Arial', 12))
        label_text.setWordWrap(True)
        scrollArea = QScrollArea()
        scrollArea.setWidget(label_text)
        layout.addRow(scrollArea)
        # Page Example
        page_example = QWidget(self)
        layout_ex = QFormLayout()
        page_example.setLayout(layout_ex)
        layout_ex.addRow(QLabel(
            f'Шифрование сообщения по алгоритму рюкзачной криптосистемы'))
        layout_ex.addRow(QLabel('Введи значения:'))
        self.inp_ex_w = QLineEdit()
        self.inp_ex_v = QLineEdit()
        self.inp_ex_m = QLineEdit()
        self.inp_ex_text = QLineEdit()
        btn_ex = QPushButton("Решить")
        btn_ex.clicked.connect(self.click_btn_ex)
        self.outp_ex = QTextBrowser()
        self.inp_ex_w.setFixedSize(620, 20)
        self.inp_ex_v.setFixedSize(620, 20)
        self.inp_ex_m.setFixedSize(620, 20)
        self.inp_ex_text.setFixedSize(620, 20)
        layout_ex.addRow(QLabel('w = '), self.inp_ex_w)
        layout_ex.addRow(QLabel('v = '), self.inp_ex_v)
        layout_ex.addRow(QLabel('m = '), self.inp_ex_m)
        layout_ex.addRow(QLabel('text = '), self.inp_ex_text)
        layout_ex.addRow(btn_ex)
        layout_ex.addRow(QLabel('Результат:'))
        layout_ex.addRow(self.outp_ex)
        # Page Task
        page_task = QWidget(self)
        layout_tsk = QFormLayout()
        page_task.setLayout(layout_tsk)
        layout_tsk.addRow(QLabel('Проверка шифрования сообщения по алгоритму рюкзачной криптосистемы'))
        self.v_tsk_v, self.v_tsk_m, self.v_tsk_w, self.v_tsk_text = get_task_val()
        self.task_text = QLabel(
            f'Зашифруй сообщение: \ntext = {self.v_tsk_text} \nw = {self.v_tsk_w} \nv = {self.v_tsk_v}) \nm = {self.v_tsk_m})')
        self.task_text.setAlignment(QtCore.Qt.AlignCenter)
        self.task_text.setFixedSize(620,160)
        self.inp_tsk = QLineEdit()
        btn_tsk_chk = QPushButton("Проверить")
        btn_tsk_rst = QPushButton("Обновить")
        self.outp_tsk = QTextBrowser()
        btn_tsk_chk.clicked.connect(self.click_btn_tsk_chk)
        btn_tsk_rst.clicked.connect(self.click_btn_tsk_rst)
        layout_tsk.addRow(self.task_text)
        layout_tsk.addRow(QLabel('Ввведи значение:'), self.inp_tsk)
        layout_tsk.addRow(btn_tsk_chk)
        layout_tsk.addRow(btn_tsk_rst)
        layout_tsk.addRow(QLabel('Результат:'))
        layout_tsk.addRow(self.outp_tsk)

        tab.addTab(page_text, 'Теория')
        tab.addTab(page_example, 'Примеры')
        tab.addTab(page_task, 'Задачи')
        
        main_layout.addWidget(tab, 0, 0, 2, 1)

    def click_btn_ex(self):
        try:
            v_exmpl_a = int(self.inp_ex_a.text())
            v_exmpl_b = int(self.inp_ex_b.text())
            v_exmpl_n = int(self.inp_ex_n.text())
            self.outp_ex.setText('')
            self.inp_ex_a.clear()
            self.inp_ex_b.clear()
            self.inp_ex_n.clear()
            self.update()
        except ValueError:
            self.outp_ex.setText(f"Введи значения: \na, b, n - целые числa")
            self.update()
    
    def click_btn_tsk_chk(self):
        try:
            inp_tsk = str(self.inp_tsk.text())
            v_tsk = ks.ks_encrypt(self.v_tsk_v, self.v_tsk_m, self.v_tsk_w, self.v_tsk_text)
            if (inp_tsk == v_tsk):
                self.outp_tsk.setText(
                    f"")
            else:
                self.outp_tsk.setText(
                    f"Неверно")
            self.inp_tsk.clear()
            self.update()
        except ValueError:
            self.outp_tsk.setText(f"Введи значения: ")
            self.update()

    def click_btn_tsk_rst(self):
        try:
            self.v_tsk_v, self.v_tsk_m, self.v_tsk_w, self.v_tsk_text = get_task_val()
            self.task_text.setText(
                f'Зашифруй сообщение: \ntext = {self.v_tsk_text} \nw = {self.v_tsk_w} \nv = {self.v_tsk_v}) \nm = {self.v_tsk_m})')
            self.inp_tsk.clear()
            self.update()
        except ValueError:
            print(ValueError)


def win_3_3(w):
    
    w.window = Window_3_3()
    w.window.show()

