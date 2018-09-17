# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(280, 143)
        self.ExecButton = QtWidgets.QPushButton(Dialog)
        self.ExecButton.setGeometry(QtCore.QRect(50, 110, 75, 23))
        self.ExecButton.setObjectName("ExecButton")
        self.CloseButton = QtWidgets.QPushButton(Dialog)
        self.CloseButton.setGeometry(QtCore.QRect(150, 110, 75, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.LoadFileSelect = QtWidgets.QPushButton(Dialog)
        self.LoadFileSelect.setGeometry(QtCore.QRect(250, 19, 21, 23))
        self.LoadFileSelect.setText("")
        self.LoadFileSelect.setObjectName("LoadFileSelect")
        self.LoadFilePath = QtWidgets.QLineEdit(Dialog)
        self.LoadFilePath.setGeometry(QtCore.QRect(10, 20, 241, 20))
        self.LoadFilePath.setObjectName("LoadFilePath")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 4, 91, 16))
        self.label.setObjectName("label")
        self.ColNum = QtWidgets.QSpinBox(Dialog)
        self.ColNum.setGeometry(QtCore.QRect(12, 46, 61, 22))
        self.ColNum.setMaximum(999)
        self.ColNum.setObjectName("ColNum")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 50, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 80, 50, 12))
        self.label_3.setObjectName("label_3")
        self.RowNum = QtWidgets.QSpinBox(Dialog)
        self.RowNum.setGeometry(QtCore.QRect(12, 76, 61, 22))
        self.RowNum.setMaximum(999)
        self.RowNum.setObjectName("RowNum")

        self.retranslateUi(Dialog)
        self.ExecButton.clicked.connect(Dialog.exec)
        self.CloseButton.clicked.connect(Dialog.reject)
        self.LoadFileSelect.clicked.connect(Dialog.LoadFileSelect_Click)
        Dialog.finished['int'].connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ExecButton.setText(_translate("Dialog", "実行"))
        self.CloseButton.setText(_translate("Dialog", "閉じる"))
        self.label.setText(_translate("Dialog", "AsciiGridファイル"))
        self.label_2.setText(_translate("Dialog", "行数"))
        self.label_3.setText(_translate("Dialog", "列数"))

