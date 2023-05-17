# This Python file uses the following encoding: windows-1251

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
import My_DiscrtLog as dis
from execution_times import get_values, method_mean_execution_time

methods = ['����� ������������','����� ���']


class Window_2_3(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('���: ����� ����������')
        self.setFixedSize(760, 800)
        self.setFont(QFont('Arial', 12))
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        self.inp_method = QComboBox()
        self.inp_method.addItems(methods)
        self.inp_tests = QLineEdit()
        self.inp_lb = QLineEdit()
        self.inp_rb = QLineEdit()
        btn = QPushButton("���������")
        btn.clicked.connect(self.click_btn)
        self.outp = QTextBrowser()

        main_layout.addWidget(QLabel('������� ������� ������� ������ ����������� ����������������'), 0, 0, 2, 2)
        main_layout.addWidget(QLabel('������ �����:'),                                               2, 0)
        main_layout.addWidget(self.inp_method,                                                       2, 1)
        main_layout.addWidget(QLabel('����� ���������� ������:'),                                    3, 0)
        main_layout.addWidget(self.inp_tests,                                                        3, 1)
        main_layout.addWidget(QLabel('�������� ��������'),                                           4, 0, 1, 2)
        main_layout.addWidget(QLabel('����� �������:'),                                              5, 0)
        main_layout.addWidget(self.inp_lb,                                                           5, 1)
        main_layout.addWidget(QLabel('������ �������:'),                                             6, 0)
        main_layout.addWidget(self.inp_rb,                                                           6, 1)
        main_layout.addWidget(btn,                                                                   7, 0, 1, 2)
        main_layout.addWidget(QLabel('���������:'),                                                  8, 0, 1, 2)
        main_layout.addWidget(self.outp,                                                             9, 0, 1, 2)

    def click_btn(self):
        try:
            self.outp.setText('')
            v_method = self.inp_method.currentText()
            v_tests = int(self.inp_tests.text())
            v_lb = int(self.inp_lb.text())
            v_rb = int(self.inp_rb.text())
            self.inp_tests.clear()
            val = get_values(v_tests, v_lb, v_rb)
            if (v_method == methods[0]):
                res = method_mean_execution_time(dis.coherence_method, val)
            elif(v_method == methods[1]):
                res = method_mean_execution_time(dis.sylvester_pohlig_hellman_method, val)
            outp = f"�����: {v_method}\n���������� ������: {v_tests}\n�������� ��������: [{v_lb}, {v_rb}]"
            outp += f"\n����� ����������: {res} ������"
            self.inp_lb.clear()
            self.inp_rb.clear()
            self.outp.setText(outp)
            self.update()
        except ValueError:
            self.outp.setText(f"����� ��������")
            self.update()


def win_2_3(w):
    
    w.window = Window_2_3()
    w.window.show()

