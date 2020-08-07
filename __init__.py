from PyQt5 import QtWidgets
import client_ui
import sys
import client
import client_window
from threading import Thread


my_client = None
my_client_window = None


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    global my_client_window
    global my_client
    my_client_window = client_window.ClientWindow()
    my_client_window.connectButton.clicked.connect(connect_to)
    my_client_window.DisconnectButton.clicked.connect(disconnect)
    my_client_window.sendButton.clicked.connect(send)

    sys.exit(app.exec_())


def connect_to():
    print("connect")
    global my_client_window
    global my_client

    if my_client is None:
        my_client = client.Client()
        my_client.cm.to_log_sygnal.connect(log_app)

    addr = (my_client_window.hostEdit.text(), int(my_client_window.portEdit.text()))
    if my_client.connect(addr):
        # thread = Thread(target=my_client.receive, daemon=True)
        # thread.start()
        my_client_window.DisconnectButton.setEnabled(True)
        my_client_window.connectButton.setEnabled(False)
        log_app("Connect to " + str(addr[0]) + ":" + str(addr[1]))
    else:
        log_app("Error connecting to " + str(addr[0]) + ":" + str(addr[1]))


def disconnect():
    global my_client
    if my_client is not None:
        my_client.send("#quit")
        # my_client.disconnect()
        # my_client = None

        my_client.disconnect()
        # thread.stop()

        log_app("Disconnect from server")
        my_client_window.DisconnectButton.setEnabled(False)
        my_client_window.connectButton.setEnabled(True)


def log_app(message):
    my_client_window.log.append(message)


def send():
    global my_client
    if len(my_client_window.messageEdit.text()) > 0:
        if my_client is not None:
            my_client.send(my_client_window.messageEdit.text())
            log_app("Me: " + my_client_window.messageEdit.text())
            my_client_window.messageEdit.setText("")
        else:
            log_app("Error sending: " + my_client_window.messageEdit.text())
    else:
        # self.messageEdit.setText("Type message here...")
        pass


if __name__ == '__main__':
    main()
