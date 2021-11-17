from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(60, 140, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 170, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 200, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 31, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 169, 31, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 31, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(140, 240, 50, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(190, 240, 300, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 180, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Решение"))
        self.label.setText(_translate("Dialog", "формула"))
        self.label_2.setText(_translate("Dialog", "1"))
        self.label_3.setText(_translate("Dialog", "2"))
        self.label_4.setText(_translate("Dialog", "3"))
        self.label_5.setText(_translate("Dialog", "Ответ:"))
        self.label_6.setText(_translate("Dialog", "?"))
        self.pushButton.setText(_translate("Dialog", "Решение"))


class MyDialog3(QtWidgets.QDialog, Ui_Dialog3):
    def __init__(self, var):
        super().__init__()
        self.var = var
        self.setupUi(self)
        self.label.setText(var)
        self.label_2.setText(var[0])
        self.label_3.setText(var[4])
        self.label_4.setText("x₀")
        self.pushButton.clicked.connect(self.run1)

    def run1(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        c = self.lineEdit_3.text()

        def isint(s):
            try:
                float(s)
                return True
            except ValueError:
                return False

        opr1 = False
        opr2 = False
        opr3 = False
        self.label_5.setText("Ответ:")
        if isint(a) and isint(b) and not isint(c):
            opr1 = True
        if isint(a) and not isint(b) and isint(c):
            opr2 = True
        if not isint(a) and isint(b) and isint(c):
            opr3 = True
        otvet = "?"
        if opr1:
            a = float(a)
            b = float(b)
            otvet = "x₀ = {}".format(str(b - a))
        elif opr2:
            a = float(a)
            c = float(c)
            otvet = "{} = {}".format(self.var[4], str(a + c))
        elif opr3:
            b = float(b)
            c = float(c)
            otvet = "{} = {}".format(self.var[0], str(b - c))
        else:
            self.label_5.setText("Ошибка:")
            otvet = "Неверно введены данные"
        self.label_6.setText(otvet)
