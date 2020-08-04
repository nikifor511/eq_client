import client
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread

class UiForm(object):
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

        self.my_client = None

    def connectToHost(self):
        addr = (self.hostEdit.text(), int(self.portEdit.text()))
        self.my_client = client.Client()
        self.my_client.cm.to_log_sygnal.connect(self.log_append)
        if self.my_client.connect(addr):
            thread = Thread(target=self.my_client.receive, daemon=True)
            thread.start()



            self.DisconnectButton.setEnabled(True)
            self.connectButton.setEnabled(False)
            self.log.append("Connect to " + str(addr[0]) + ":" + str(addr[1]))
        else:
            self.log.append("Error connecting to " + str(addr[0]) + ":" + str(addr[1]))

    def disconnectToHost(self):
        # addr = (self.hostEdit.text(), int(self.portEdit.text()))
        self.my_client.disconnect()
        self.my_client = None

        self.log.append("Disconnect from server")
        self.DisconnectButton.setEnabled(False)
        self.connectButton.setEnabled(True)

    def log_append(self, message):
        self.log.append(message)
