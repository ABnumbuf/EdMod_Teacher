# This Python file uses the following encoding: windows-1251

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
import My_DiscrtLog as dis
from util import read_text, get_values



class Window_2_1(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('ЗДЛ: Метод согласования')
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
        text = read_text('text_mod2_block1.html')
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        scrollArea = QScrollArea()
        scrollArea.setWidget(label_text)
        layout.addRow(scrollArea)
        # Page Example
        page_example = QWidget(self)
        layout_ex = QFormLayout()
        page_example.setLayout(layout_ex)
        layout_ex.addRow(QLabel(f'<p>Решение задачи <box>a<sup>x</sup></box> &#8801; b (mod p)<p> методом согласования'))
        layout_ex.addRow(QLabel('Введи значения:'))
        self.inp_ex_a = QLineEdit()
        self.inp_ex_b = QLineEdit()
        self.inp_ex_n = QLineEdit()
        btn_ex = QPushButton("Решить")
        btn_ex.clicked.connect(self.click_btn_ex)
        self.outp_ex = QTextBrowser()
        self.inp_ex_a.setFixedSize(620,20)
        self.inp_ex_b.setFixedSize(620,20)
        self.inp_ex_n.setFixedSize(620,20)
        layout_ex.addRow(QLabel('a = '), self.inp_ex_a)
        layout_ex.addRow(QLabel('b = '), self.inp_ex_b)
        layout_ex.addRow(QLabel('n = '), self.inp_ex_n)
        layout_ex.addRow(btn_ex)
        layout_ex.addRow(QLabel('Вывод:'))
        layout_ex.addRow(self.outp_ex)
        # Page Task
        page_task = QWidget(self)
        layout_tsk = QFormLayout()
        page_task.setLayout(layout_tsk)
        layout_tsk.addRow(QLabel('Проверка решения ЗДЛ методом согласования'))
        self.v_tsk_a,self.v_tsk_b,self.v_tsk_n = get_values(1)[0]
        self.task_text = QLabel(
            f'<p>Реши задачу: <box>{str(self.v_tsk_a)}<sup>x</sup></box> &#8801; {str(self.v_tsk_b)} (mod {str(self.v_tsk_n)})<p>')
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
        layout_tsk.addRow(QLabel('Вывод:'))
        layout_tsk.addRow(self.outp_tsk)

        # add pane to the tab widget
        tab.addTab(page_text, 'Теория')
        tab.addTab(page_example, 'Примеры')
        tab.addTab(page_task, 'Задачи')
        
        main_layout.addWidget(tab, 0, 0, 2, 1)

    def click_btn_ex(self):
        try:
            # v_exmpl_m = str(self.inp_ex_m.text())
            # v_exmpl_p = int(self.inp_ex_p.text())
            # v_exmpl_g = int(self.inp_ex_g.text())
            # v_exmpl_r = int(self.inp_ex_r.text())
            # v_exmpl_s = int(self.inp_ex_s.text())
            # v_exmpl_y = int(self.inp_ex_y.text())
            # self.outp_ex.setText(elg.check_ds_ElGamal_outp(v_exmpl_m, v_exmpl_r, v_exmpl_s,v_exmpl_y, v_exmpl_g, v_exmpl_p))
            self.update()
        except ValueError:
            self.outp_ex.setText(f"Введи значения: \nm - строка \np, g, y, r, s - целые числa")
            self.update()
    
    def click_btn_tsk_chk(self):
        try:
            # v_tsk = str(self.inp_tsk.currentText())
            # res = elg.check_ds_ElGamal(self.v_tsk_m, self.v_tsk_r, self.v_tsk_s, self.v_tsk_y, self.v_tsk_g, self.v_tsk_p)
            # if ((res and v_tsk =='Подпись подлина') or 
            #         (not res and v_tsk =='Подпись подделана')):
            #     self.outp_tsk.setText(
            #         f"p = {self.v_tsk_p}, g = {self.v_tsk_g}, y = {self.v_tsk_y}, \nm = {self.v_tsk_m}, \nr = {self.v_tsk_r}, s = {self.v_tsk_s}\nВерно\n{v_tsk}")
            # else:
            #     self.outp_tsk.setText(
            #         f"p = {self.v_tsk_p}, g = {self.v_tsk_g}, y = {self.v_tsk_y}, \nm = {self.v_tsk_m}, \nr = {self.v_tsk_r}, s = {self.v_tsk_s}\nНеверно\n{v_tsk}")
            self.update()
        except ValueError:
            self.outp_tsk.setText(f"Ввери ответ")
            self.update()

    def click_btn_tsk_rst(self):
        try:
            self.v_tsk_m, self.v_tsk_p, self.v_tsk_g, self.v_tsk_y, self.v_tsk_r, self.v_tsk_s = get_task_val()
            self.task_text.setText(
                f'Являеется ли подпись правильной для: \np = {self.v_tsk_p}, g = {self.v_tsk_g}, y = {self.v_tsk_y}, \nm = {self.v_tsk_m}, \nr = {self.v_tsk_r}, s = {self.v_tsk_s}')
            self.update()
        except ValueError:
            print(ValueError)


def win_2_1(w):
    
    w.window = Window_2_1()
    w.window.show()

