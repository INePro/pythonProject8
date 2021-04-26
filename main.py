from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit
from  PyQt5 import QtWidgets


class MainWindow(QMainWindow):
    def __init__(self, parent=None): #Конструктор класса
        super().__init__()

        self.setMinimumSize(300, 300)  # Устанавливаем размеры
        self.setWindowTitle("HZ")  # Устанавливаем заголовок окна

        self.ButOn()

        self.arr = [[2,2,2],
                    [2,2,2],
                    [2,2,2]]
        a = 0

    def ButOn(self):
        self.but1 = QPushButton(" ", self)
        self.but1.move(0,0)
        self.but1.resize(100, 100)
        self.but1.clicked.connect(self.b1)

        self.but2 = QPushButton(' ', self)
        self.but2.move(100, 0)
        self.but2.resize(100, 100)

        self.but3 = QPushButton(" ", self)
        self.but3.move(200, 0)
        self.but3.resize(100, 100)

        self.but4 = QPushButton(' ', self)
        self.but4.move(0, 100)
        self.but4.resize(100, 100)

        self.but5 = QPushButton(" ", self)
        self.but5.move(100, 100)
        self.but5.resize(100, 100)

        self.but6 = QPushButton(' ', self)
        self.but6.move(200, 100)
        self.but6.resize(100, 100)

        self.but7 = QPushButton(" ", self)
        self.but7.move(0, 200)
        self.but7.resize(100, 100)

        self.but8 = QPushButton(' ', self)
        self.but8.move(100, 200)
        self.but8.resize(100, 100)

        self.but9 = QPushButton(' ', self)
        self.but9.move(200, 200)
        self.but9.resize(100, 100)

    def b1(self):
        self.a+=1
        if self.a%2==0:
            self.arr[0][0]=0
        else:
            self.arr[0][0]=1
#        print(self.arr)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())