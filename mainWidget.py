# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt




class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(593, 539)
        self.connectButton = QtWidget.QPushButton(Form)
        self.connectButton.setGeometry(QtCore.QRect(10, 10, 80, 25))
        self.connectButton.setObjectName("connectButton")
        self.hostEdit = QtWidgets.QLineEdit(Form)
        self.hostEdit.setGeometry(QtCore.QRect(100, 10, 81, 25))
        self.hostEdit.setObjectName("hostEdit")
        self.portEdit = QtWidgets.QLineEdit(Form)
        self.portEdit.setGeometry(QtCore.QRect(190, 10, 51, 25))
        self.portEdit.setObjectName("portEdit")
        self.logEdit = QtWidgets.QTextEdit(Form)
        self.logEdit.setGeometry(QtCore.QRect(10, 40, 571, 431))
        self.logEdit.setObjectName("logEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 480, 431, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.sendButton = QtWidgets.QPushButton(Form)
        self.sendButton.setGeometry(QtCore.QRect(500, 480, 80, 25))
        self.sendButton.setObjectName("sendButton")
        self.disconnectButton = QtWidgets.QPushButton(Form)
        self.disconnectButton.setGeometry(QtCore.QRect(500, 10, 80, 25))
        self.disconnectButton.setObjectName("disconnectButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.connectButton, self.hostEdit)
        Form.setTabOrder(self.hostEdit, self.portEdit)
        Form.setTabOrder(self.portEdit, self.disconnectButton)
        Form.setTabOrder(self.disconnectButton, self.logEdit)
        Form.setTabOrder(self.logEdit, self.lineEdit_3)
        Form.setTabOrder(self.lineEdit_3, self.sendButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.connectButton.setText(_translate("Form", "Connect"))
        self.hostEdit.setText(_translate("Form", "127.0.0.1"))
        self.portEdit.setText(_translate("Form", "58583"))
        self.sendButton.setText(_translate("Form", "Send"))
        self.disconnectButton.setText(_translate("Form", "Disconnect"))
