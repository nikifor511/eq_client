from socket import AF_INET, socket, SOCK_STREAM
from PyQt5.QtCore import QObject, pyqtSignal


BUFSIZ = 1024

class Client(QObject):
    class commu(QObject):
        to_log_sygnal = pyqtSignal(['QString'])

    def __init__(self):
        super(Client, self).__init__()
        self.cm = self.commu()
        self.to_log = self.cm.to_log_sygnal
        self.sock = socket(AF_INET, SOCK_STREAM)
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

    def send(self, event=None):
        """ Handles sending of messages. """
        msg = "hi"
        self.sock.send(bytes(msg, "utf8"))
        if msg == "#quit":
            self.sock.close()
            # top.quit()

    def connect(self, ADDR):
        try:
            # sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect(ADDR)
        except :
            print("[Errno 111] Connection refused")
            return False

        return True
        # receive_thread = Thread(target=receive)
        # receive_thread.start()

    def disconnect(self):
        self.sock.close()