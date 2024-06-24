import sys
import os
from check import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QSize
import math as m


class MyWin(QtWidgets.QMainWindow):
    def k(self, x):
        return m.log(1.1 + m.tan(x/2))

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Integral)  # функция кнопки вычислить
        self.ui.pushButton.clicked.connect(self.left_rectangle_method)
        self.ui.pushButton.clicked.connect(self.right_rectangle_method)
        self.ui.action.triggered.connect(self.Info)  # Вешаем на "Об авторах" функцию Info

    def Info(self):
        QMessageBox.about(self, "Об авторе", "Программа была написана \n Доровиным Андреем Владимировичем\n 2023-ФГиИБ-ПИ-1б")

    def Integral(self):
        self.ui.label_5.setText('')
        s1 = 1
        s2 = 0
        Iter = 0
        a = int(self.ui.textEdit.toPlainText())
        b = int(self.ui.textEdit_2.toPlainText())
        n = 4
        i = 0
        eps = float(self.ui.textEdit_3.toPlainText())
        while abs(s2 - s1) >= eps:
            s1 = s2
            s2 = 0
            n = n * 2
            h = (b - a) / n
            Iter += 1
            i = 0
            while i < n:
                x = a + h * (i + 0.5)
                k = m.log(1.1 + m.tan(x/2))
                s2 += abs(k * h)
                i += 1
        Otvet = "\nЗначение интеграла: " + str("%.3f" % s2) + "\nКоличество итераций: " + str(Iter)
        self.ui.label_5.setText(Otvet)

    def left_rectangle_method(self):
        self.ui.label_7.setText('')
        s1 = 1
        s2 = 0
        Iter = 0
        a = int(self.ui.textEdit.toPlainText())
        b = int(self.ui.textEdit_2.toPlainText())
        n = 4
        i = 0
        eps = float(self.ui.textEdit_3.toPlainText())
        while abs(s2 - s1) >= eps:
            s1 = s2
            s2 = 0
            n = n * 2
            h = (b - a) / n
            Iter += 1
            i = 0
            while i < n:
                x = a + h * i
                k = m.log(1.1 + m.tan(x/2))
                s2 += abs(k * h)
                i += 1
        Otvet = "\nЗначение интеграла: " + str("%.3f" % s2) + "\nКоличество итераций: " + str(Iter)
        self.ui.label_7.setText(Otvet)

    def right_rectangle_method(self):
        self.ui.label_8.setText('')
        s1 = 1
        s2 = 0
        Iter = 0
        a = int(self.ui.textEdit.toPlainText())
        b = int(self.ui.textEdit_2.toPlainText())
        n = 4
        i = 0
        eps = float(self.ui.textEdit_3.toPlainText())
        while abs(s2 - s1) >= eps:
            s1 = s2
            s2 = 0
            n = n * 2
            h = (b - a) / n
            Iter += 1
            i = 0
            while i < n:
                x = a + h * (i + 1)
                k = m.log(1.1 + m.tan(x/2))
                s2 += abs(k * h)
                i += 1
        Otvet = "\nЗначение интеграла: " + str("%.3f" % s2) + "\nКоличество итераций: " + str(Iter)
        self.ui.label_8.setText(Otvet)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
