from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit
from  PyQt5 import QtWidgets
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self, parent=None): #Конструктор класса
        super().__init__()

        self.setMinimumSize(300, 300)  # Устанавливаем размеры
        self.setWindowTitle("HZ")  # Устанавливаем заголовок окна

        self.ButOn()

        self.arr = np.array([[2,2,2],
                             [2,2,2],
                             [2,2,2]])
        self.a = 0

    def ButOn(self):
        self.but1 = QPushButton(" ", self)
        self.but1.move(0,0)
        self.but1.resize(100, 100)
        self.but1.clicked.connect(self.b1)

        self.but2 = QPushButton(' ', self)
        self.but2.move(100, 0)
        self.but2.resize(100, 100)
        self.but2.clicked.connect(self.b2)

        self.but3 = QPushButton(" ", self)
        self.but3.move(200, 0)
        self.but3.resize(100, 100)
        self.but3.clicked.connect(self.b3)

        self.but4 = QPushButton(' ', self)
        self.but4.move(0, 100)
        self.but4.resize(100, 100)
        self.but4.clicked.connect(self.b4)

        self.but5 = QPushButton(" ", self)
        self.but5.move(100, 100)
        self.but5.resize(100, 100)
        self.but5.clicked.connect(self.b5)

        self.but6 = QPushButton(' ', self)
        self.but6.move(200, 100)
        self.but6.resize(100, 100)
        self.but6.clicked.connect(self.b6)

        self.but7 = QPushButton(" ", self)
        self.but7.move(0, 200)
        self.but7.resize(100, 100)
        self.but7.clicked.connect(self.b7)

        self.but8 = QPushButton(' ', self)
        self.but8.move(100, 200)
        self.but8.resize(100, 100)
        self.but8.clicked.connect(self.b8)

        self.but9 = QPushButton(' ', self)
        self.but9.move(200, 200)
        self.but9.resize(100, 100)
        self.but9.clicked.connect(self.b9)


    def b1(self):
        self.a+=1
        if self.a%2==0:
            self.arr[0][0]=0
        else:
            self.arr[0][0]=1
        self.check()

    def b2(self):
        self.a+=1
        if self.a%2==0:
            self.arr[0][1]=0
        else:
            self.arr[0][1]=1
        self.check()

    def b3(self):
        self.a += 1
        if self.a % 2 == 0:
            self.arr[0][2] = 0
        else:
            self.arr[0][2] = 1
        self.check()

    def b4(self):
        self.a += 1
        if self.a % 2 == 0:
            self.arr[1][0] = 0
        else:
            self.arr[1][0] = 1
        self.check()

    def b5(self):
        self.a += 1
        if self.a % 2 == 0:
            self.arr[1][1] = 0
        else:
            self.arr[1][1] = 1
        self.check()

    def b6(self):
        self.a += 1
        if self.a % 2 == 0:
            self.arr[1][2] = 0
        else:
            self.arr[1][2] = 1
        self.check()

    def b7(self):
        self.a += 1
        if self.a % 2 == 0:
            self.arr[2][0] = 0
        else:
            self.arr[2][0] = 1
        self.check()

    def b8(self):
        self.a += 1
        if self.a % 2 == 0:
            self.arr[2][1] = 0
        else:
            self.arr[2][1] = 1
        self.check()

    def b9(self):
        self.a += 1
        if self.a % 2 == 0:
            self.arr[2][2] = 0
        else:
            self.arr[2][2] = 1
            print(self.arr)
        self.check()

    def check(self):
        print(self.arr)
        if np.all(np.fliplr(self.arr).diagonal()==0) or np.all(self.arr.diagonal()==0) or np.all(self.arr[0,:]==0) or np.all(self.arr[1,:]==0) or np.all(self.arr[2,:]==0) or np.all(self.arr[:,0]==0) or np.all(self.arr[:,1]==0) or np.all(self.arr[:,2]==0):
            print("You win 0")
            exit()
        elif np.all(np.fliplr(self.arr).diagonal()==1) or np.all(self.arr.diagonal()==1) or np.all(self.arr[0,:]==1) or np.all(self.arr[1,:]==1) or np.all(self.arr[2,:]==1) or np.all(self.arr[:,0]==1) or np.all(self.arr[:,1]==1) or np.all(self.arr[:,2]==1):
            print("Win 1")
            exit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    print(MainWindow)
    sys.exit(app.exec())