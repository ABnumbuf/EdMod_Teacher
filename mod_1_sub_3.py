# This Python file uses the following encoding: windows-1251

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
import random
from util import read_text
import My_ElGamal as elg

def get_task_val():
    v_tsk_y, v_tsk_p, v_tsk_g, v_tsk_x = elg.get_keys_ElGamal(10, 100)
    flag = random.randint(0, 1)
    if (flag):
        v_tsk_x = v_tsk_p + 6
    v_tsk_m = elg.get_random_message(6)
    v_tsk_r, v_tsk_s = elg.ds_ElGamal(v_tsk_m, v_tsk_p, v_tsk_g, v_tsk_x)
    return v_tsk_m, v_tsk_p, v_tsk_g, v_tsk_y, v_tsk_r, v_tsk_s

class Window_1_3(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('��� �� ����� ���-������: ��������� �������')
        self.setFixedSize(700,800)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        # create a tab widget
        tab = QTabWidget(self)
        tab.setFont(QFont('Arial', 14))
        # Page Theory
        page_text = QWidget(self)
        layout = QFormLayout()
        page_text.setLayout(layout)
        text = read_text('text_mod1_block3.html')
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        scrollArea = QScrollArea()
        scrollArea.setWidget(label_text)
        layout.addRow(scrollArea)
        # Page Example
        page_example = QWidget(self)
        layout_ex = QFormLayout()
        page_example.setLayout(layout_ex)
        layout_ex.addRow(QLabel('��������� ��� �� ����� ���-������ �� ��������� ���������'))
        layout_ex.addRow(QLabel('����� ��������:'))
        self.inp_ex_m = QLineEdit()
        self.inp_ex_p = QLineEdit()
        self.inp_ex_g = QLineEdit()
        self.inp_ex_y = QLineEdit()
        self.inp_ex_r = QLineEdit()
        self.inp_ex_s = QLineEdit()
        btn_ex = QPushButton("������")
        btn_ex.clicked.connect(self.click_btn_ex)
        self.outp_ex = QTextBrowser()
        self.inp_ex_m.setFixedSize(620,20)
        self.inp_ex_p.setFixedSize(620,20)
        self.inp_ex_g.setFixedSize(620,20)
        self.inp_ex_y.setFixedSize(620,20)
        self.inp_ex_r.setFixedSize(620,20)
        self.inp_ex_s.setFixedSize(620,20)
        layout_ex.addRow(QLabel('m = '), self.inp_ex_m)
        layout_ex.addRow(QLabel('p = '), self.inp_ex_p)
        layout_ex.addRow(QLabel('g = '), self.inp_ex_g)
        layout_ex.addRow(QLabel('y = '), self.inp_ex_y)
        layout_ex.addRow(QLabel('r = '), self.inp_ex_r)
        layout_ex.addRow(QLabel('s = '), self.inp_ex_s)
        layout_ex.addRow(btn_ex)
        layout_ex.addRow(QLabel('�����:'))
        layout_ex.addRow(self.outp_ex)
        # Page Task
        page_task = QWidget(self)
        layout_tsk = QFormLayout()
        page_task.setLayout(layout_tsk)
        layout_tsk.addRow(QLabel('�������� ��������� ��� ���-������ �� �������� ���������'))
        self.v_tsk_m, self.v_tsk_p, self.v_tsk_g, self.v_tsk_y, self.v_tsk_r, self.v_tsk_s = get_task_val()
        self.task_text = QLabel(
            f'��������� �� ������� ���������� ���: \np = {self.v_tsk_p}, g = {self.v_tsk_g}, y = {self.v_tsk_y}, \nm = {self.v_tsk_m}, \nr = {self.v_tsk_r}, s = {self.v_tsk_s}')
        self.task_text.setAlignment(QtCore.Qt.AlignCenter)
        self.task_text.setFixedSize(620,160)
        self.inp_tsk = QComboBox()
        self.inp_tsk.addItems(['������� �������', '������� ���������'])
        btn_tsk_chk = QPushButton("���������")
        btn_tsk_rst = QPushButton("��������")
        self.outp_tsk = QTextBrowser()
        btn_tsk_chk.clicked.connect(self.click_btn_tsk_chk)
        btn_tsk_rst.clicked.connect(self.click_btn_tsk_rst)

        layout_tsk.addRow(self.task_text)

        layout_tsk.addRow(QLabel('������:'), self.inp_tsk)
        layout_tsk.addRow(btn_tsk_chk)
        layout_tsk.addRow(btn_tsk_rst)
        layout_tsk.addRow(QLabel('�����:'))
        layout_tsk.addRow(self.outp_tsk)

        # add pane to the tab widget
        tab.addTab(page_text, '������')
        tab.addTab(page_example, '�������')
        tab.addTab(page_task, '������')
        
        main_layout.addWidget(tab, 0, 0, 2, 1)

    def click_btn_ex(self):
        try:
            v_exmpl_m = str(self.inp_ex_m.text())
            v_exmpl_p = int(self.inp_ex_p.text())
            v_exmpl_g = int(self.inp_ex_g.text())
            v_exmpl_r = int(self.inp_ex_r.text())
            v_exmpl_s = int(self.inp_ex_s.text())
            v_exmpl_y = int(self.inp_ex_y.text())
            self.outp_ex.setText(elg.check_ds_ElGamal_outp(v_exmpl_m, v_exmpl_r, v_exmpl_s,v_exmpl_y, v_exmpl_g, v_exmpl_p))
            self.update()
        except ValueError:
            self.outp_ex.setText(f"����� ��������: \nm - ������ \np, g, y, r, s - ����� ����a")
            self.update()
    
    def click_btn_tsk_chk(self):
        try:
            v_tsk = str(self.inp_tsk.currentText())
            res = elg.check_ds_ElGamal(self.v_tsk_m, self.v_tsk_r, self.v_tsk_s, self.v_tsk_y, self.v_tsk_g, self.v_tsk_p)
            if ((res and v_tsk =='������� �������') or 
                    (not res and v_tsk =='������� ���������')):
                self.outp_tsk.setText(
                    f"p = {self.v_tsk_p}, g = {self.v_tsk_g}, y = {self.v_tsk_y}, \nm = {self.v_tsk_m}, \nr = {self.v_tsk_r}, s = {self.v_tsk_s}\n�����\n{v_tsk}")
            else:
                self.outp_tsk.setText(
                    f"p = {self.v_tsk_p}, g = {self.v_tsk_g}, y = {self.v_tsk_y}, \nm = {self.v_tsk_m}, \nr = {self.v_tsk_r}, s = {self.v_tsk_s}\n�������\n{v_tsk}")
            self.update()
        except ValueError:
            self.outp_tsk.setText(f"����� �����")
            self.update()

    def click_btn_tsk_rst(self):
        try:
            self.v_tsk_m, self.v_tsk_p, self.v_tsk_g, self.v_tsk_y, self.v_tsk_r, self.v_tsk_s = get_task_val()
            self.task_text.setText(
                f'��������� �� ������� ���������� ���: \np = {self.v_tsk_p}, g = {self.v_tsk_g}, y = {self.v_tsk_y}, \nm = {self.v_tsk_m}, \nr = {self.v_tsk_r}, s = {self.v_tsk_s}')
            self.update()
        except ValueError:
            print(ValueError)


def win_1_3(w):
    
    w.window = Window_1_3()
    w.window.show()

