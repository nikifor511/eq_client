import tkinter
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt
import random, sys


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
            "Hola Mundo", "Привет мир"]

        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # Connecting the signal
        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


def receive():
    """ Handles receiving of messages. """
    while True:
        try:
            msg = sock.recv(BUFSIZ).decode("utf8")
            # msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):
    """ Handles sending of messages. """
    msg = "hi"
    sock.send(bytes(msg, "utf8"))
    if msg == "#quit":
        sock.close()
        # top.quit()


# def on_closing(event=None):
#     """ This function is to be called when the window is closed. """
#     my_msg.set("#quit")
#     send()
#
#
# def smiley_button_tieup(event=None):
#     """ Function for smiley button action """
#     my_msg.set(":)")    # A common smiley character
#     send()
#
#
# def sad_button_tieup(event=None):
#     """ Function for smiley button action """
#     my_msg.set(":(")    # A common smiley character
#     send()


# top = tkinter.Tk()
# top.title("Simple Chat Client v1.0")
# messages_frame = tkinter.Frame(top)
#
# my_msg = tkinter.StringVar()  # For the messages to be sent.
# my_msg.set("")
# scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# msg_list = tkinter.Listbox(messages_frame, height=15, width=70, yscrollcommand=scrollbar.set)
# scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
# msg_list.pack()
#
# messages_frame.pack()
#
# button_label = tkinter.Label(top, text="Enter Message:")
# button_label.pack()
# entry_field = tkinter.Entry(top, textvariable=my_msg, foreground="Red")
# entry_field.bind("<Return>", send)
# entry_field.pack()
# send_button = tkinter.Button(top, text="Send", command=send)
# send_button.pack()
# smiley_button = tkinter.Button(top, text=":)", command=smiley_button_tieup)
# smiley_button.pack()
# sad_button = tkinter.Button(top, text=":(", command=sad_button_tieup)
# sad_button.pack()
#
# quit_button = tkinter.Button(top, text="Quit", command=on_closing)
# quit_button.pack()
#
# top.protocol("WM_DELETE_WINDOW", on_closing)

app = QApplication(sys.argv)

widget = MyWidget()
widget.resize(800, 600)
widget.show()

sys.exit(app.exec_())

HOST = "127.0.0.1"
PORT = 58583
BUFSIZ = 1024
ADDR = (HOST, PORT)
sock = socket(AF_INET, SOCK_STREAM)
try:
    sock.connect(ADDR)
except ConnectionRefusedError:
    print("[Errno 111] Connection refused")

receive_thread = Thread(target=receive)
receive_thread.start()
# tkinter.mainloop()  # Starts GUI execution.