import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication,QLineEdit, QTextEdit
from PyQt5.QtCore import QCoreApplication, QRect


class ClientWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.connectButton = QPushButton("Connect", self)
        self.hostEdit = QLineEdit(self)
        self.portEdit = QLineEdit(self)
        self.DisconnectButton = QPushButton(self)
        self.log = QTextEdit(self)
        self.messageEdit = QLineEdit(self)
        self.sendButton = QPushButton(self)
        self.init_ui()

    def init_ui(self):
        self.connectButton.setGeometry(QRect(10, 10, 75, 23))
        self.connectButton = QPushButton("Connect", self)
        self.connectButton.setGeometry(QRect(10, 10, 75, 23))
        # connectButton.setObjectName("connectButton")
        # self.connectButton.clicked.connect(self.connectToHost)

        self.hostEdit.setGeometry(QRect(90, 10, 151, 20))
        self.hostEdit.setText("127.0.0.1")
        # hostEdit.setObjectName("hostEdit")

        self.portEdit.setGeometry(QRect(250, 10, 51, 20))
        self.portEdit.setText("58583")
        # self.portEdit.setObjectName("portEdit")

        self.DisconnectButton.setGeometry(QRect(310, 10, 81, 23))
        self.DisconnectButton.setText("Disconnect")
        # self.DisconnectButton.setObjectName("DisconnectButton")
        self.DisconnectButton.setEnabled(False)
        # self.DisconnectButton.clicked.connect(self.disconnectToHost)

        self.log.setGeometry(QRect(10, 40, 381, 221))
        # self.log.setObjectName("log")

        self.messageEdit.setGeometry(QRect(10, 270, 301, 20))
        self.messageEdit.setObjectName("messageEdit")

        self.sendButton.setGeometry(QRect(320, 270, 75, 23))
        self.sendButton.setText("Send")
        # self.sendButton.clicked.connect(self.send)

        self.setGeometry(600, 300, 400, 300)
        self.setWindowTitle('__CLIENT__')
        self.show()