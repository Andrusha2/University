import sys
from check import *
from PyQt5.QtWidgets import QMessageBox
from math import log, tan


class MyWin(QtWidgets.QMainWindow):
    @staticmethod
    def k(x):
        return log(1.1 + tan(x/2))

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        self.ui.pushButton.clicked.connect(self.integral)  # функция кнопки вычислить
        self.ui.pushButton.clicked.connect(self.left_rectangle_method)
        self.ui.pushButton.clicked.connect(self.right_rectangle_method)
        self.ui.action.triggered.connect(self.info)  # Вешаем на "Об авторах" функцию Info

    def info(self):
        QMessageBox.about(self, "Об авторе", "Программа была написана \n Доровиным Андреем Владимировичем"
                                             "\n 2023-ФГиИБ-ПИ-1б")

    def integral(self):
        self.ui.label_5.setText('')
        s1 = 1
        s2 = 0
        iteration = 0
        a = int(self.ui.textEdit.toPlainText())
        b = int(self.ui.textEdit_2.toPlainText())
        n = 4
        eps = float(self.ui.textEdit_3.toPlainText())
        while abs(s2 - s1) >= eps:
            s1 = s2
            s2 = 0
            n = n * 2
            h = (b - a) / n
            iteration += 1
            i = 0
            while i < n:
                x = a + h * (i + 0.5)
                k = log(1.1 + tan(x/2))
                s2 += abs(k * h)
                i += 1
        answer = "\nЗначение интеграла: " + str("%.3f" % s2) + "\nКоличество итераций: " + str(iteration)
        self.ui.label_5.setText(answer)

    def left_rectangle_method(self):
        self.ui.label_7.setText('')
        s1 = 1
        s2 = 0
        iteration = 0
        a = int(self.ui.textEdit.toPlainText())
        b = int(self.ui.textEdit_2.toPlainText())
        n = 4
        eps = float(self.ui.textEdit_3.toPlainText())
        while abs(s2 - s1) >= eps:
            s1 = s2
            s2 = 0
            n = n * 2
            h = (b - a) / n
            iteration += 1
            i = 0
            while i < n:
                x = a + h * i
                k = log(1.1 + tan(x/2))
                s2 += abs(k * h)
                i += 1
        answer = "\nЗначение интеграла: " + str("%.3f" % s2) + "\nКоличество итераций: " + str(iteration)
        self.ui.label_7.setText(answer)

    def right_rectangle_method(self):
        self.ui.label_8.setText('')
        s1 = 1
        s2 = 0
        iteration = 0
        a = int(self.ui.textEdit.toPlainText())
        b = int(self.ui.textEdit_2.toPlainText())
        n = 4
        eps = float(self.ui.textEdit_3.toPlainText())
        while abs(s2 - s1) >= eps:
            s1 = s2
            s2 = 0
            n = n * 2
            h = (b - a) / n
            iteration += 1
            i = 0
            while i < n:
                x = a + h * (i + 1)
                k = log(1.1 + tan(x/2))
                s2 += abs(k * h)
                i += 1
        answer = "\nЗначение интеграла: " + str("%.3f" % s2) + "\nКоличество итераций: " + str(iteration)
        self.ui.label_8.setText(answer)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
