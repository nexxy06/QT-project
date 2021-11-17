from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogu(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(455, 376)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 30, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 21, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 21, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 21, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 21, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 160, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 190, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 220, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 250, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(140, 310, 51, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(200, 310, 211, 16))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "формула"))
        self.label_2.setText(_translate("Dialog", "1"))
        self.label_3.setText(_translate("Dialog", "2"))
        self.label_4.setText(_translate("Dialog", "3"))
        self.label_5.setText(_translate("Dialog", "4"))
        self.pushButton.setText(_translate("Dialog", "Решение"))
        self.label_6.setText(_translate("Dialog", "Ответ:"))
        self.label_7.setText(_translate("Dialog", " ?"))


class MyDialogu(QtWidgets.QDialog, Ui_Dialogu):
    def __init__(self, var):
        super().__init__()
        self.var = var
        self.setupUi(self)
        self.label.setText(var)
        self.label_2.setText(var[0])
        self.v = 0
        if var == "a = (V-V₀)/t":
            self.label_3.setText("V")
            self.label_4.setText("V₀")
            self.label_5.setText("t")
            self.v = 1
        elif var == "V = V₀ + a*t":
            self.label_3.setText("V₀")
            self.label_4.setText("a")
            self.label_5.setText("t")
            self.v = 2
        elif var == "s=(V²-V₀²)/2a":
            self.label_3.setText("V")
            self.label_4.setText("V₀")
            self.label_5.setText("a")
            self.v = 3
        elif var == "R = (p*l)/S":
            self.label_3.setText("p")
            self.label_4.setText("l")
            self.label_5.setText("S")
            self.v = 4
        elif var == "s=V₀*t+(a*t²)/2":
            self.label_3.setText("V₀")
            self.label_4.setText("t")
            self.label_5.setText("a")
            self.v = 5
        self.pushButton.clicked.connect(self.run1)

    def run1(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        c = self.lineEdit_3.text()
        d = self.lineEdit_4.text()

        def isint(s):
            try:
                float(s)
                return True
            except ValueError:
                return False

        opr1 = False
        opr2 = False
        opr3 = False
        opr4 = False
        self.label_6.setText("Ответ:")
        if not isint(a) and isint(b) and isint(c) and isint(d):
            opr1 = True
        if isint(a) and not isint(b) and isint(c) and isint(d):
            opr2 = True
        if isint(a) and isint(b) and not isint(c) and isint(d):
            opr3 = True
        if isint(a) and isint(b) and isint(c) and not isint(d):
            opr4 = True
        otvet = "?"
        if self.v == 1:
            if opr1:
                c = float(c)
                b = float(b)
                d = float(d)
                otvet = "a = {}".format((b - c) / d)
            elif opr2:
                a = float(a)
                c = float(c)
                d = float(d)
                otvet = "V = {}".format(a * d + c)
            elif opr3:
                a = float(a)
                b = float(b)
                d = float(d)
                otvet = "V₀ = {}".format(b - (a * d))
            elif opr4:
                a = float(a)
                b = float(b)
                c = float(c)
                otvet = "t = {}".format((b - c) / a)
            else:
                self.label_6.setText("Ошибка:")
                otvet = "Неверно введены данные"
        elif self.v == 2:
            if opr1:
                c = float(c)
                b = float(b)
                d = float(d)
                otvet = "V = {}".format(b + c * d)
            elif opr2:
                a = float(a)
                c = float(c)
                d = float(d)
                otvet = "V₀ = {}".format(a - c * d)
            elif opr3:
                a = float(a)
                b = float(b)
                d = float(d)
                otvet = "a = {}".format((a - b) / d)
            elif opr4:
                a = float(a)
                b = float(b)
                c = float(c)
                otvet = "t = {}".format((a - b) / c)
            else:
                self.label_6.setText("Ошибка:")
                otvet = "Неверно введены данные"
        elif self.v == 3:
            if opr1:
                c = float(c)
                b = float(b)
                d = float(d)
                otvet = "s = {}".format((b ** 2 - c ** 2) / 2 * d)
            elif opr2:
                a = float(a)
                c = float(c)
                d = float(d)
                otvet = "V = +-{}".format((a * d * 2 + c ** 2) ** 0.5)
            elif opr3:
                a = float(a)
                b = float(b)
                d = float(d)
                otvet = "V₀ = +-{}".format((b ** 2 - a * d * 2) ** 0.5)
            elif opr4:
                a = float(a)
                b = float(b)
                c = float(c)
                otvet = "a = {}".format(a / (b ** 2 - c ** 2) * 2)
            else:
                self.label_6.setText("Ошибка:")
                otvet = "Неверно введены данные"
        elif self.v == 4:
            if opr1:
                c = float(c)
                b = float(b)
                d = float(d)
                otvet = "R = {}".format((b * c) / d)
            elif opr2:
                a = float(a)
                c = float(c)
                d = float(d)
                otvet = "p = {}".format(a * d / c)
            elif opr3:
                a = float(a)
                b = float(b)
                d = float(d)
                otvet = "l = {}".format(a * d / b)
            elif opr4:
                a = float(a)
                b = float(b)
                c = float(c)
                otvet = "s = {}".format(b * c / a)
            else:
                self.label_6.setText("Ошибка:")
                otvet = "Неверно введены данные"
        elif self.v == 5:
            if opr1:
                c = float(c)
                b = float(b)
                d = float(d)
                otvet = "s = {}".format(b * c + (d * c ** 2) / 2)
            elif opr2:
                a = float(a)
                c = float(c)
                d = float(d)
                otvet = "V₀ = {}".format((a - (d * c ** 2) / 2) / c)
            elif opr3:
                a = float(a)
                b = float(b)
                d = float(d)
                if b == 0:
                    otvet = "t = {}".format((a * 2 / d) ** 0.5)
                else:
                    otvet = "нет возможности высчитать"
            elif opr4:
                a = float(a)
                b = float(b)
                c = float(c)
                otvet = "a = {}".format(2 * (a - b * c) / c ** 2)
            else:
                self.label_6.setText("Ошибка:")
                otvet = "Неверно введены данные"
        self.label_7.setText(otvet)
