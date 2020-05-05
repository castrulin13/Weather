# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pogoda(object):
    def setupUi(self, Pogoda):
        Pogoda.setObjectName("Pogoda")
        Pogoda.resize(259, 264)
        Pogoda.setStyleSheet("background-color: #362727;\n"
"font: 16pt \"Arial\";")
        self.lineEdit = QtWidgets.QLineEdit(Pogoda)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 241, 31))
        self.lineEdit.setStyleSheet("color: #c44343;\n"
"font: 75 14pt \"Arial\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Pogoda)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 241, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"border: none;\n"
"font: 75 14pt \"Arial\";\n"
"color: #d42a2a;\n"
"background-color: #915c5c;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #d42a2a;\n"
"    color: #915c5c;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Pogoda)
        self.label.setGeometry(QtCore.QRect(10, 110, 241, 21))
        self.label.setStyleSheet("color:#d62b2b;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Pogoda)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 241, 21))
        self.label_2.setStyleSheet("color:#d62b2b;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Pogoda)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 241, 21))
        self.label_3.setStyleSheet("color:#d62b2b;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Pogoda)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 241, 21))
        self.label_4.setStyleSheet("color:#d62b2b;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Pogoda)
        QtCore.QMetaObject.connectSlotsByName(Pogoda)

    def retranslateUi(self, Pogoda):
        _translate = QtCore.QCoreApplication.translate
        Pogoda.setWindowTitle(_translate("Pogoda", "Dialog"))
        self.pushButton.setText(_translate("Pogoda", "Узнать"))
