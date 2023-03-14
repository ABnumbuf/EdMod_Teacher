# This Python file uses the following encoding: windows-1251

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
import My_Knapsack as ks
from util import read_text, get_random_message, extended_gcd
import random


def get_task_val():
    v_tsk_v = [x ** random.randint(1,3) for x in range(2, random.randint(5,6))]
    v_tsk_v.sort()
    v_tsk_m = random.randint(2, 90)
    v_tsk_w = random.randint(2, 40)
    while extended_gcd(v_tsk_m,v_tsk_w)[0] == 1:
        v_tsk_m = random.randint(2, 90)
        v_tsk_w = random.randint(2, 40)
    v_tsk_text = get_random_message(6)
    return v_tsk_v, v_tsk_m, v_tsk_w, v_tsk_text.upper()


class Window_3_2(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('��������� �������������: �������� ����������')
        self.setFixedSize(700, 800)
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        tab = QTabWidget(self)
        tab.setFont(QFont('Arial', 12))
        # Page Theory
        page_text = QWidget(self)
        layout = QFormLayout()
        page_text.setLayout(layout)
        text = read_text('text_mod3_block2.html')
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
            f'���������� ��������� �� ��������� ��������� �������������'))
        layout_ex.addRow(QLabel('����� ��������:'))
        self.inp_ex_w = QLineEdit()
        self.inp_ex_v = QLineEdit()
        self.inp_ex_m = QLineEdit()
        self.inp_ex_text = QLineEdit()
        btn_ex = QPushButton("������")
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
        layout_ex.addRow(QLabel('���������:'))
        layout_ex.addRow(self.outp_ex)
        # Page Task
        page_task = QWidget(self)
        layout_tsk = QFormLayout()
        page_task.setLayout(layout_tsk)
        layout_tsk.addRow(QLabel('�������� ���������� �� ��������� ��������� �������������'))
        self.v_tsk_v, self.v_tsk_m, self.v_tsk_w, self.v_tsk_text = get_task_val()
        self.task_text = QLabel(
            f'�������� ���������: \ntext = {self.v_tsk_text} \nw = {self.v_tsk_w} \nv = {self.v_tsk_v} \nm = {self.v_tsk_m}')
        self.task_text.setAlignment(QtCore.Qt.AlignCenter)
        self.task_text.setFixedSize(620, 160)
        self.inp_tsk = QLineEdit()
        btn_tsk_chk = QPushButton("���������")
        btn_tsk_rst = QPushButton("��������")
        self.outp_tsk = QTextBrowser()
        btn_tsk_chk.clicked.connect(self.click_btn_tsk_chk)
        btn_tsk_rst.clicked.connect(self.click_btn_tsk_rst)
        layout_tsk.addRow(self.task_text)
        layout_tsk.addRow(QLabel('������ �����:'), self.inp_tsk)
        layout_tsk.addRow(btn_tsk_chk)
        layout_tsk.addRow(btn_tsk_rst)
        layout_tsk.addRow(QLabel('���������:'))
        layout_tsk.addRow(self.outp_tsk)

        tab.addTab(page_text, '������')
        tab.addTab(page_example, '�������')
        tab.addTab(page_task, '������')
        
        main_layout.addWidget(tab, 0, 0, 2, 1)

    def click_btn_ex(self):
        try:
            v_exmpl_v = [int(i) for i in str(self.inp_ex_v.text()).split(',')]
            v_exmpl_w = int(self.inp_ex_w.text())
            v_exmpl_m = int(self.inp_ex_m.text())
            v_exmpl_text = str(self.inp_ex_text.text())
            self.outp_ex.setText(
                f"v = {v_exmpl_v}\nw = {v_exmpl_w}\nm = {v_exmpl_m}\n�������� �����: {v_exmpl_text}\n{ks.ks_encrypt_outp(v_exmpl_v,v_exmpl_m,v_exmpl_w,v_exmpl_text)}")
            self.inp_ex_w.clear()
            self.inp_ex_v.clear()
            self.inp_ex_m.clear()
            self.inp_ex_text.clear()
            self.update()
        except ValueError:
            self.outp_ex.setText(f"����� ��������: \nm, w - ����� ����a \nv - ������������������ ����� ����� (�������������� �����) \ntext - ������")
            self.update()
    
    def click_btn_tsk_chk(self):
        try:
            inp_tsk = [int(i) for i in str(self.inp_tsk.text()).split(',')]
            v_tsk = ks.ks_encrypt(self.v_tsk_v, self.v_tsk_m, self.v_tsk_w, self.v_tsk_text)
            if (inp_tsk == v_tsk):
                self.outp_tsk.setText(
                    f"{inp_tsk} = {v_tsk}\n�����")
            else:
                self.outp_tsk.setText(
                    f"{inp_tsk} != {v_tsk}\n�������")
            self.inp_tsk.clear()
            self.update()
        except ValueError:
            self.outp_tsk.setText(f"����� �����: ���������")
            self.update()

    def click_btn_tsk_rst(self):
        try:
            self.v_tsk_v, self.v_tsk_m, self.v_tsk_w, self.v_tsk_text = get_task_val()
            self.task_text.setText(
                f'�������� ���������: \ntext = {self.v_tsk_text} \nw = {self.v_tsk_w} \nv = {self.v_tsk_v} \nm = {self.v_tsk_m}')
            self.inp_tsk.clear()
            self.update()
        except ValueError:
            print(ValueError)


def win_3_2(w):
    
    w.window = Window_3_2()
    w.window.show()

