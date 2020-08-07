# from socket import AF_INET, socket, SOCK_STREAM
import socket
from PyQt5.QtCore import QObject, pyqtSignal
from threading import Thread

BUFSIZ = 1024


class Client(QObject):

    class commu(QObject):
        to_log_sygnal = pyqtSignal(['QString'])

    def __init__(self):
        super(Client, self).__init__()
        self.cm = self.commu()
        self.to_log = self.cm.to_log_sygnal
        self.sock = None

        # self.to_log = pyqtSignal(int)

    def receive(self):
        """ Handles receiving of messages. """
        while True:
            try:
                msg = self.sock.recv(BUFSIZ).decode("utf8")

                print(str(msg))
                self.cm.to_log_sygnal.emit(str(msg))
                # msg_list.insert(tkinter.END, msg)

            except OSError:  # Possibly client has left the chat.
                break

    def send(self, message, event=None):
        """ Handles sending of messages. """
        try:
            self.sock.send(bytes(message, "utf8"))
            return True
        except:
            return False

    def connect(self, ADDR):
        if self.sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            # sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect(ADDR)
        except :
            print("[Errno 111] Connection refused")
            return False

        receive_thread = Thread(target=self.receive, daemon=True)
        receive_thread.start()
        return True

    def disconnect(self):
        self.sock.close()
        self.sock = None
