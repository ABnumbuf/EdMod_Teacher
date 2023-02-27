

import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
from util import read_text
import mod_1_sub_1, mod_1_sub_2
# , mod_1_sub_3, \
#     mod_2_sub_1, mod_2_sub_2, mod_2_sub_3, \
#     mod_3_sub_1, mod_3_sub_2, mod_3_sub_3

mods = ['ЭЦП по схеме Эль-Гамаля'
        ,'Задача Дискретного Логарифмирования'
        ,'Рюкзачная Криптосистема']
sub_1 = ['Генерация Ключей'
        ,'Создание Подписи'
        ,'Валидация Подписи']
sub_2 = ['Метод Согласования'
        ,'Метод СПХ'
        ,'Время Выполнения']
sub_3 = ['Задача о Рюкзаке'
        ,'Алгоритм Шифрования'
        ,'Алгоритм Дешифрования']


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('EdMod')
        self.setFixedSize(700,300)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        # create a tab widget
        tab = QWidget(self)
        tab.setFont(QFont('Arial', 12))

        layout = QFormLayout()
        tab.setLayout(layout)

        lb1 = QLabel("EdMod")
        lb2 = QLabel("Криптографические Методы")
        lb1.setFont(QFont('Arial', 52))
        lb1.setAlignment(QtCore.Qt.AlignHCenter)
        lb2.setFont(QFont('Arial', 12))
        lb2.setAlignment(QtCore.Qt.AlignHCenter)
        lb2.setFixedHeight(100)
        layout.addRow(lb1)
        layout.addRow(lb2)

        self.cmb = QComboBox()
        self.cmb.addItems(mods)
        self.cmb.setFixedSize(550,24)


        self.btn = QPushButton("Далее")
        self.btn.clicked.connect(self.click_btn)

        layout.addRow(self.cmb, self.btn)

        main_layout.addWidget(tab, 0, 0, 2, 1)

        self.show()

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
            else:
                if   choosed == sub_1[0]: mod_1_sub_1.__name__
                elif choosed == sub_1[1]: mod_1_sub_2
                # elif choosed == sub_1[2]: mod_1_sub_3.win_1_3()
                # elif choosed == sub_2[0]: mod_2_sub_1.win_2_1()
                # elif choosed == sub_2[1]: mod_2_sub_2.win_2_2()
                # elif choosed == sub_2[2]: mod_2_sub_3.win_2_3()
                # elif choosed == sub_3[0]: mod_3_sub_1.win_3_1()
                # elif choosed == sub_3[1]: mod_3_sub_2.win_3_2()
                # elif choosed == sub_3[2]: mod_3_sub_3.win_3_3()
            self.update()
        except ValueError:
            print(f"ERROR")
    
    def click_btn_strt(self):
        try:
            choosed = 0
            if choosed == mods[0]:
                print(1)
        except ValueError:
            print(f"ERROR")
    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
