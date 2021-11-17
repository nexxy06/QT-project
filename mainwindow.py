import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from dialogwindow import MyDialog
from dialog2 import MyDialog2
from dialog3 import MyDialog3
from dialog4 import MyDialog4
from dialoguni import MyDialogu
from dialogslo import MyDialogs


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 120, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 120, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 200, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 240, 101, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 320, 111, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 240, 101, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 280, 131, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(450, 240, 101, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(250, 320, 111, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(450, 200, 101, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(450, 160, 101, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(450, 120, 101, 41))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(250, 200, 101, 41))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(250, 280, 101, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(450, 40, 101, 41))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(350, 40, 101, 41))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(350, 80, 101, 41))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(450, 80, 101, 41))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(250, 40, 101, 41))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(250, 80, 101, 41))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(350, 160, 101, 41))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(250, 160, 101, 41))
        self.pushButton_22.setObjectName("pushButton_22")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 10, 141, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(80, 200, 93, 28))
        self.pushButton_23.setObjectName("pushButton_23")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(21, 21, 219, 169))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(21, 237, 135, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 400, 350, 16))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(21, 260, 219, 170))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 576, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Помощник по физике"))
        self.pushButton.setText(_translate("MainWindow", "s = V * t"))
        self.pushButton_2.setText(_translate("MainWindow", "s = x - x₀"))
        self.pushButton_3.setText(_translate("MainWindow", "a = (V-V₀)/t"))
        self.pushButton_4.setText(_translate("MainWindow", "V = V₀ + a*t"))
        self.pushButton_5.setText(_translate("MainWindow", "s=V₀*t+(a*t²)/2"))
        self.pushButton_6.setText(_translate("MainWindow", "s=(V²-V₀²)/2a"))
        self.pushButton_7.setText(_translate("MainWindow", "x=x₀+V₀*t+(a*t²)/2"))
        self.pushButton_8.setText(_translate("MainWindow", "a = F / m"))
        self.pushButton_9.setText(_translate("MainWindow", "F=G*(m₁*m²)/R²"))
        self.pushButton_10.setText(_translate("MainWindow", "a = V²/ R"))
        self.pushButton_11.setText(_translate("MainWindow", "p = m * V"))
        self.pushButton_12.setText(_translate("MainWindow", "T = 1 / V"))
        self.pushButton_13.setText(_translate("MainWindow", "λ = V * T"))
        self.pushButton_14.setText(_translate("MainWindow", "p = m / V"))
        self.pushButton_15.setText(_translate("MainWindow", "F = m * g"))
        self.pushButton_16.setText(_translate("MainWindow", "F = k * x"))
        self.pushButton_17.setText(_translate("MainWindow", "P = m * g"))
        self.pushButton_18.setText(_translate("MainWindow", "p = F / S"))
        self.pushButton_19.setText(_translate("MainWindow", "I = q / t"))
        self.pushButton_20.setText(_translate("MainWindow", "U = A / q"))
        self.pushButton_21.setText(_translate("MainWindow", "I = U / R"))
        self.pushButton_22.setText(_translate("MainWindow", "R = (p*l)/S"))
        self.label_3.setText(_translate("MainWindow", "Подходящие формулы:"))
        self.pushButton_23.setText(_translate("MainWindow", "Поиск"))
        self.label_2.setText(_translate("MainWindow", "Возможные величины:"))
        self.label.setText(_translate("MainWindow", ""))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\""
                                            " \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" "
                                            "/><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'"
                                            "MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400;"
                                            " font-style:normal;\">\n"
                                            "<p style=\" margin-top:12px; margin-bottom:12px;"
                                            " margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                                            " text-indent:0px; background-color:#2b2b2b;"
                                            "\"><span style=\" font-family:\'JetBrains Mono,monospace\'"
                                            "; font-size:8pt; color:#a9b7c6; background-color:#2b2b2b;\""
                                            ">скорость V</span><span style=\" font-family:"
                                            "\'JetBrains Mono,monospace\'; font-size:8pt; color:#a9b7c6;"
                                            "\"><br />начальная скорость V₀<br />путь s<br />время t<br />"
                                            "координата x<br />начальная координата x₀<br />"
                                            "ускорение a<br />сила F<br />масса m<br />радиус R<br />"
                                            "гравитационная G<br />импульс p<br />период T<br />"
                                            "длина волны λ<br />расстояние между телами R<br />"
                                            "плотность p<br />объем V<br />ускорение свободного падения g<br />"
                                            "жёсткость k<br />удлинение тела x<br />вес P<br />давление p<br />"
                                            "площадь S<br />расстояние s<br />сила тока I<br />"
                                            "электрический заряд q<br />напряжение U<br />работа A<br />"
                                            "сопротивление R<br />длина l<br />"
                                            "удельное сопротивление p</span></p></body></html>"))


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.pushButton_23.clicked.connect(self.run)
        self.pushButton.clicked.connect(self.puB)
        self.pushButton_8.clicked.connect(self.puB)
        self.pushButton_11.clicked.connect(self.puB)
        self.pushButton_13.clicked.connect(self.puB)
        self.pushButton_14.clicked.connect(self.puB)
        self.pushButton_15.clicked.connect(self.puB)
        self.pushButton_16.clicked.connect(self.puB)
        self.pushButton_17.clicked.connect(self.puB)
        self.pushButton_18.clicked.connect(self.puB)
        self.pushButton_19.clicked.connect(self.puB)
        self.pushButton_20.clicked.connect(self.puB)
        self.pushButton_21.clicked.connect(self.puB)

        self.pushButton_10.clicked.connect(self.puB2)
        self.pushButton_2.clicked.connect(self.puB3)
        self.pushButton_12.clicked.connect(self.puB4)

        self.pushButton_22.clicked.connect(self.puBu)
        self.pushButton_6.clicked.connect(self.puBu)
        self.pushButton_4.clicked.connect(self.puBu)
        self.pushButton_3.clicked.connect(self.puBu)
        self.pushButton_5.clicked.connect(self.puBu)

        self.pushButton_7.clicked.connect(self.puBs)
        self.pushButton_9.clicked.connect(self.puBs)

    def run(self):
        slo = {"скорость": "V", "начальная скорость": "V₀", "путь": "s", "время": "t", "координата": "x",
               "начальная координата": "x₀", "ускорение": "a", "сила": "F", "масса": "m", "радиус": "R",
               "гравитационная": "G", "импульс": "p", "период": "T", "длина волны": "λ", "расстояние между т.": "R",
               "плотность": "p", "объем": "V", "ускор. свободного падения": "g", "жёсткость": "k",
               "удлинение тела": "x", "вес": "P", "давление": "p", "площадь": "S", "сила тока": "I",
               "электри. заряд": "q", "напряжение": "U",
               "работа": "A", "сопротивление": "R", "длина": "l", "удельное сопротивление": "p"}
        lis = self.textEdit.toPlainText().splitlines()
        li = []
        for i in lis:
            if i not in slo:
                self.label.setText("Ошибка: такая величина не найдена в листе")
                break
            else:
                self.label.setText("")
            li.append(slo[i])
        self.pushButton.show()
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.pushButton_4.show()
        self.pushButton_5.show()
        self.pushButton_6.show()
        self.pushButton_7.show()
        self.pushButton_8.show()
        self.pushButton_9.show()
        self.pushButton_10.show()
        self.pushButton_11.show()
        self.pushButton_12.show()
        self.pushButton_13.show()
        self.pushButton_14.show()
        self.pushButton_15.show()
        self.pushButton_16.show()
        self.pushButton_17.show()
        self.pushButton_18.show()
        self.pushButton_19.show()
        self.pushButton_20.show()
        self.pushButton_21.show()
        self.pushButton_22.show()
        for j in li:
            if j not in self.pushButton.text():
                self.pushButton.hide()
            if j not in self.pushButton_2.text():
                self.pushButton_2.hide()
            if j not in self.pushButton_3.text():
                self.pushButton_3.hide()
            if j not in self.pushButton_4.text():
                self.pushButton_4.hide()
            if j not in self.pushButton_5.text():
                self.pushButton_5.hide()
            if j not in self.pushButton_6.text():
                self.pushButton_6.hide()
            if j not in self.pushButton_7.text():
                self.pushButton_7.hide()
            if j not in self.pushButton_8.text():
                self.pushButton_8.hide()
            if j not in self.pushButton_9.text():
                self.pushButton_9.hide()
            if j not in self.pushButton_10.text():
                self.pushButton_10.hide()
            if j not in self.pushButton_11.text():
                self.pushButton_11.hide()
            if j not in self.pushButton_12.text():
                self.pushButton_12.hide()
            if j not in self.pushButton_13.text():
                self.pushButton_13.hide()
            if j not in self.pushButton_14.text():
                self.pushButton_14.hide()
            if j not in self.pushButton_15.text():
                self.pushButton_15.hide()
            if j not in self.pushButton_16.text():
                self.pushButton_16.hide()
            if j not in self.pushButton_17.text():
                self.pushButton_17.hide()
            if j not in self.pushButton_18.text():
                self.pushButton_18.hide()
            if j not in self.pushButton_19.text():
                self.pushButton_19.hide()
            if j not in self.pushButton_20.text():
                self.pushButton_20.hide()
            if j not in self.pushButton_21.text():
                self.pushButton_21.hide()
            if j not in self.pushButton_22.text():
                self.pushButton_22.hide()

    def puB(self):
        self.dialog1 = MyDialog(self.sender().text())
        self.dialog1.show()

    def puB2(self):
        self.dialog2 = MyDialog2(self.sender().text())
        self.dialog2.show()

    def puB3(self):
        self.dialog3 = MyDialog3(self.sender().text())
        self.dialog3.show()

    def puB4(self):
        self.dialog4 = MyDialog4(self.sender().text())
        self.dialog4.show()

    def puBu(self):
        self.dialogu = MyDialogu(self.sender().text())
        self.dialogu.show()

    def puBs(self):
        self.dialogs = MyDialogs(self.sender().text())
        self.dialogs.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
