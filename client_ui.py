import client
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
from PyQt5.QtCore import QObject, pyqtSignal


class UiForm(object):

    class signals(QObject):
        connect_signal = pyqtSignal([tuple])




    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.connectButton = QtWidgets.QPushButton(Form)
        self.connectButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.connectButton.setText("Connect")
        self.connectButton.setObjectName("connectButton")
        self.connectButton.clicked.connect(self.connectToHost)

        self.hostEdit = QtWidgets.QLineEdit(Form)
        self.hostEdit.setGeometry(QtCore.QRect(90, 10, 151, 20))
        self.hostEdit.setText("127.0.0.1")
        self.hostEdit.setObjectName("hostEdit")

        self.portEdit = QtWidgets.QLineEdit(Form)
        self.portEdit.setGeometry(QtCore.QRect(250, 10, 51, 20))
        self.portEdit.setText("58583")
        self.portEdit.setObjectName("portEdit")

        self.DisconnectButton = QtWidgets.QPushButton(Form)
        self.DisconnectButton.setGeometry(QtCore.QRect(310, 10, 81, 23))
        self.DisconnectButton.setText("Disconnect")
        self.DisconnectButton.setObjectName("DisconnectButton")
        self.DisconnectButton.setEnabled(False)
        self.DisconnectButton.clicked.connect(self.disconnectToHost)

        self.log = QtWidgets.QTextEdit(Form)
        self.log.setGeometry(QtCore.QRect(10, 40, 381, 221))
        self.log.setObjectName("log")

        self.messageEdit = QtWidgets.QLineEdit(Form)
        self.messageEdit.setGeometry(QtCore.QRect(10, 270, 301, 20))
        self.messageEdit.setObjectName("messageEdit")

        self.sendButton = QtWidgets.QPushButton(Form)
        self.sendButton.setGeometry(QtCore.QRect(320, 270, 75, 23))
        self.sendButton.setText("Send")
        self.sendButton.clicked.connect(self.send)

        self.my_client = None


    def connectToHost(self):
        addr = (self.hostEdit.text(), int(self.portEdit.text()))
        self.sgn.connect_signal.emit(addr)




    def disconnectToHost(self):
        # addr = (self.hostEdit.text(), int(self.portEdit.text()))
        # self.my_client.send("#quit")
        self.my_client.disconnect()
        self.my_client = None

        self.log.append("Disconnect from server")
        self.DisconnectButton.setEnabled(False)
        self.connectButton.setEnabled(True)

    def log_append(self, message):
        self.log.append(message)

    def send(self):
        if len(self.messageEdit.text()) > 0:
            if self.my_client is not None:
                self.my_client.send(self.messageEdit.text())
                self.log.append("Me: " + self.messageEdit.text())
                self.messageEdit.setText("")
            else:
                self.log.append("Error sending: " + self.messageEdit.text())
        else:
            # self.messageEdit.setText("Type message here...")
            pass
