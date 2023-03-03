# This Python file uses the following encoding: windows-1251

import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui
import mod_1_sub_1, mod_1_sub_2, mod_1_sub_3 \
    , mod_2_sub_1 , mod_2_sub_2, mod_2_sub_3 \
    , mod_3_sub_1, mod_3_sub_2, mod_3_sub_3

mods = ['ЭЦП по схеме Эль-Гамаля'
        ,'Задача дискретного логарифмирования'
        ,'Рюкзачная криптосистема']
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
        self.setFixedSize(725, 300)
        self.setFont(QFont('Arial', 12))
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        lb1 = QLabel("EdMod")
        lb1.setStyleSheet('color: #FFCB69')
        lb2 = QLabel("Криптографические методы")
        self.lb3 = QLabel("Выбери раздел")
        lb1.setFont(QFont('Arial', 50))
        lb1.setAlignment(QtCore.Qt.AlignHCenter)
        lb2.setAlignment(QtCore.Qt.AlignHCenter)
        self.lb3.setAlignment(QtCore.Qt.AlignHCenter)
        lb2.setFixedHeight(125)
        self.cmb = QComboBox()
        self.cmb.addItems(mods)
        self.btn = QPushButton("Далее")
        self.btn.clicked.connect(self.click_btn)
        self.btn.setFixedSize(100, 35)
        main_layout.addWidget(lb1, 0, 0, 1, 2)
        main_layout.addWidget(lb2, 1, 0, 1, 2)
        main_layout.addWidget(self.lb3, 2, 0, 1, 2)
        main_layout.addWidget(self.cmb, 3, 0, 2, 1)
        main_layout.addWidget(self.btn, 3, 1)


    def click_btn(self):
        try:
            choosed = self.cmb.currentText()
            print(choosed)
            if choosed in mods:
                self.cmb.clear()
                if choosed == mods[0]:
                    self.cmb.addItems(sub_1)
                elif choosed == mods[1]:
                    self.cmb.addItems(sub_2)
                elif choosed == mods[2]:
                    self.cmb.addItems(sub_3)
                self.btn.setText('Начать')
                self.lb3.setText(f'Выбери подраздел [{choosed}]')
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
    dark_palette.setColor(QtGui.QPalette.Background, QtGui.QColor(51, 50, 50))
    dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(61, 60, 60))
    dark_palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(255, 255, 235))
    dark_palette.setColor(QtGui.QPalette.BrightText, QtGui.QColor(255, 255, 235))
    dark_palette.setColor(QtGui.QPalette.Text, QtGui.QColor(255, 255, 235))
    dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(255, 218, 133))
    dark_palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(31, 30, 30))
    dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(255, 218, 133))
    dark_palette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(31, 30, 30))

    # app.setPalette(dark_palette)

    window = MainWindow()
    window.show()
    app.exec()
