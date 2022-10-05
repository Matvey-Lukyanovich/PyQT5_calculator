from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = []
        self.operand_1 = []
        self.operand_2 = []

    def initUI(self):
        self.setGeometry(300, 300, 280, 375)
        self.setWindowTitle("Calculator")
        self.setStyleSheet('border: 8px solid black; background-color: gray')

        self.label = QLabel(self)
        self.label.setText('0')
        self.label.setStyleSheet('border: 1px solid black; background-color: white')
        self.label.setFont(QFont('Arial', 14))
        self.label.resize(270, 40)
        self.label.move(5, 25)
        self.move(200, 200)

        self.num_1 = QPushButton('1', self)
        self.num_1.resize(50, 50)
        self.num_1.move(5, 100)
        self.num_1.setStyleSheet('border: 1px solid black; background-color: white')
        self.num_1.setFont(QFont('Arial', 14))

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(50, 50)
        self.num_2.move(60, 100)
        self.num_2.setStyleSheet('border: 1px solid black; background-color: white')
        self.num_2.setFont(QFont('Arial', 14))

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(50, 50)
        self.num_3.move(115, 100)
        self.num_3.setStyleSheet('border: 1px solid black; background-color: white')
        self.num_3.setFont(QFont('Arial', 14))

        self.div = QPushButton('/', self)
        self.div.resize(50, 50)
        self.div.move(170, 100)
        self.div.setStyleSheet('border: 1px solid black; background-color: white')
        self.div.setFont(QFont('Arial', 14))

        self.mod = QPushButton('%', self)
        self.mod.resize(50, 50)
        self.mod.move(225, 100)
        self.mod.setStyleSheet('border: 1px solid black; background-color: white')
        self.mod.setFont(QFont('Arial', 14))

        self.div_2 = QPushButton('//', self)
        self.div_2.resize(50, 50)
        self.div_2.move(225, 155)
        self.div_2.setStyleSheet('border: 1px solid black; background-color: white')
        self.div_2.setFont(QFont('Arial', 14))

        self.pow2 = QPushButton('^2', self)
        self.pow2.resize(50, 50)
        self.pow2.move(225, 210)
        self.pow2.setStyleSheet('border: 1px solid black; background-color: white')
        self.pow2.setFont(QFont('Arial', 14))

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(50, 50)
        self.num_4.move(5, 155)
        self.num_4.setStyleSheet('border: 1px solid black; background-color: white')
        self.num_4.setFont(QFont('Arial', 14))

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(50, 50)
        self.num_5.move(60, 155)
        self.num_5.setStyleSheet('border: 1px solid black; background-color: white')
        self.num_5.setFont(QFont('Arial', 14))

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(50, 50)
        self.num_6.move(115, 155)
        self.num_6.setStyleSheet('border: 1px solid black; background-color: white')
        self.num_6.setFont(QFont('Arial', 14))

        self.mul = QPushButton('*', self)
        self.mul.resize(50, 50)
        self.mul.move(170, 155)
        self.mul.setStyleSheet('border: 1px solid black; background-color: white')
        self.mul.setFont(QFont('Arial', 14))

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(50, 50)
        self.num_7.move(5, 210)
        self.num_7.setStyleSheet('border: 1px solid black; background-color: white')
        self.num_7.setFont(QFont('Arial', 14))

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(50, 50)
        self.num_8.move(60, 210)
        self.num_8.setStyleSheet('border: 1px solid black; background-color: white')
        self.num_8.setFont(QFont('Arial', 14))

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(50, 50)
        self.num_9.move(115, 210)
        self.num_9.setStyleSheet('border: 1px solid black; background-color: white')
        self.num_9.setFont(QFont('Arial', 14))

        self.plus = QPushButton('+', self)
        self.plus.resize(50, 50)
        self.plus.move(170, 210)
        self.plus.setStyleSheet('border: 1px solid black; background-color: white')
        self.plus.setFont(QFont('Arial', 14))

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(50, 50)
        self.num_0.move(5, 265)
        self.num_0.setStyleSheet('border: 1px solid black; background-color: white')
        self.num_0.setFont(QFont('Arial', 14))

        self.minus = QPushButton('-', self)
        self.minus.resize(50, 50)
        self.minus.move(60, 265)
        self.minus.setStyleSheet('border: 1px solid black; background-color: white')
        self.minus.setFont(QFont('Arial', 14))

        self.step = QPushButton('^', self)
        self.step.resize(50, 50)
        self.step.move(115, 265)
        self.step.setStyleSheet('border: 1px solid black; background-color: white')
        self.step.setFont(QFont('Arial', 14))

        self.sqrt = QPushButton('√', self)
        self.sqrt.resize(50, 50)
        self.sqrt.move(170, 265)
        self.sqrt.setStyleSheet('border: 1px solid black; background-color: white')
        self.sqrt.setFont(QFont('Arial', 14))

        self.ravn = QPushButton('=', self)
        self.ravn.resize(160, 50)
        self.ravn.move(5, 320)
        self.ravn.setStyleSheet('border: 1px solid black; background-color: white')
        self.ravn.setFont(QFont('Arial', 14))

        self.c = QPushButton('C', self)
        self.c.resize(50, 50)
        self.c.move(170, 320)
        self.c.setStyleSheet('border: 1px solid black; background-color: white')
        self.c.setFont(QFont('Arial', 14))

        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minus_1)
        self.mul.clicked.connect(self.mul_1)
        self.div.clicked.connect(self.div_1)
        self.div_2.clicked.connect(self.div_22)
        self.mod.clicked.connect(self.mod_1)
        self.pow2.clicked.connect(self.pow_2)
        self.step.clicked.connect(self.step_1)
        self.sqrt.clicked.connect(self.sqrt_1)
        self.ravn.clicked.connect(self.ravno)
        self.c.clicked.connect(self.clean)

    def enterValue(self):
        if self.label.text() == '0':
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enterValue()

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def three(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def plus_1(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def minus_1(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def mul_1(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def div_1(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def mod_1(self):
        self.operation = '%'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def div_22(self):
        self.operation = '//'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def pow_2(self):
        self.label.setText(str(float(self.label.text()) * float(self.label.text())))

    def step_1(self):
        self.operation = '^'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def sqrt_1(self):
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def ravno(self):
        self.operand_2 = float(self.label.text())
        if self.operation == '+':
            self.rezult = self.operand_1 + self.operand_2
        elif self.operation == '-':
            self.rezult = self.operand_1 - self.operand_2
        elif self.operation == '*':
            self.rezult = self.operand_1 * self.operand_2
        elif self.operation == '/':
            if self.operand_2 == 0:
                self.rezult = 'error'
            else:
                self.rezult = self.operand_1 / self.operand_2
        elif self.operation == '//':
            if self.operand_2 == 0:
                self.rezult = 'error'
            else:
                self.rezult = self.operand_1 // self.operand_2
        elif self.operation == '%':
            if self.operand_2 == 0:
                self.rezult = 'error'
            else:
                self.rezult = self.operand_1 % self.operand_2
        elif self.operation == '^':
            self.rezult = self.operand_1 ** self.operand_2

        elif self.operation == '√':
            self.rezult = self.operand_1 ** (1 / self.operand_2)

        self.label.setText(str(self.rezult))

    def clean(self):
        self.label.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
