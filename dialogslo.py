from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogs(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(455, 403)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 30, 231, 51))
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
        self.label_6.setGeometry(QtCore.QRect(140, 330, 51, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(200, 330, 211, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 280, 21, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 280, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "формула"))
        self.label_2.setText(_translate("Dialog", "1"))
        self.label_3.setText(_translate("Dialog", "1"))
        self.label_4.setText(_translate("Dialog", "1"))
        self.label_5.setText(_translate("Dialog", "1"))
        self.pushButton.setText(_translate("Dialog", "Решение"))
        self.label_6.setText(_translate("Dialog", "Ответ:"))
        self.label_7.setText(_translate("Dialog", " ?"))
        self.label_8.setText(_translate("Dialog", "1"))


class MyDialogs(QtWidgets.QDialog, Ui_Dialogs):
    def __init__(self, var):
        super().__init__()
        self.var = var
        self.setupUi(self)
        self.label.setText(var)
        self.label_2.setText(var[0])
        self.v = 0
        if var == "x=x₀+V₀*t+(a*t²)/2":
            self.label_3.setText("x₀")
            self.label_4.setText("V")
            self.label_5.setText("t")
            self.label_8.setText("a")
            self.v = 1
        elif var == "F=G*(m₁*m²)/R²":
            self.label_3.setText("G")
            self.label_4.setText("m₁")
            self.label_5.setText("m")
            self.label_8.setText("R")
            self.v = 2
        self.pushButton.clicked.connect(self.run1)

    def run1(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        c = self.lineEdit_3.text()
        d = self.lineEdit_4.text()
        e = self.lineEdit_5.text()

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
        opr5 = False
        self.label_6.setText("Ответ:")
        if not isint(a) and isint(b) and isint(c) and isint(d) and isint(e):
            opr1 = True
        if isint(a) and not isint(b) and isint(c) and isint(d) and isint(e):
            opr2 = True
        if isint(a) and isint(b) and not isint(c) and isint(d) and isint(e):
            opr3 = True
        if isint(a) and isint(b) and isint(c) and not isint(d) and isint(e):
            opr4 = True
        if isint(a) and isint(b) and isint(c) and isint(d) and not isint(e):
            opr5 = True
        otvet = "?"
        if self.v == 1:
            if opr1:
                c = float(c)
                b = float(b)
                d = float(d)
                e = float(e)
                otvet = "x = {}".format(b + (c * d) + (e * d ** 2) / 2)
            elif opr2:
                a = float(a)
                c = float(c)
                d = float(d)
                e = float()
                otvet = "x₀ = {}".format(a - ((c * d) + (e * d ** 2) / 2))
            elif opr3:
                a = float(a)
                b = float(b)
                d = float(d)
                e = float(e)
                otvet = "V = {}".format((a - b - (e * d ** 2) / 2) / d)
            elif opr4:
                a = float(a)
                b = float(b)
                c = float(c)
                e = float(e)
                if c == 0:
                    otvet = "t = {}".format(((a - b) * 2 / e) ** 0.5)
                else:
                    otvet = "нет возможности высчитать"
            elif opr5:
                a = float(a)
                b = float(b)
                c = float(c)
                d = float(d)
                otvet = "a = {}".format(2 * (a - c * d - b) / d ** 2)
            else:
                self.label_6.setText("Ошибка:")
                otvet = "Неверно введены данные"
        elif self.v == 2:
            if opr1:
                c = float(c)
                b = float(b)
                d = float(d)
                e = float(e)
                otvet = "F = {}".format(b * (c * d ** 2) / e ** 2)
            elif opr2:
                a = float(a)
                c = float(c)
                d = float(d)
                e = float(e)
                otvet = "G = {}".format(a / ((c * d ** 2) / e ** 2))
            elif opr3:
                a = float(a)
                b = float(b)
                d = float(d)
                e = float(e)
                otvet = "m₁ = {}".format(a / b * e ** 2 / d ** 2)
            elif opr4:
                a = float(a)
                b = float(b)
                c = float(c)
                e = float(e)
                otvet = "m = {}".format(a / b * e ** 2 / c)
            elif opr5:
                a = float(a)
                b = float(b)
                c = float(c)
                d = float(d)
                otvet = "R = {}".format((c * d ** 2 / (a / b)) ** 0.5)
            else:
                self.label_6.setText("Ошибка:")
                otvet = "Неверно введены данные"
        self.label_7.setText(otvet)
