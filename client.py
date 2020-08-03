from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


BUFSIZ = 1024
sock = socket(AF_INET, SOCK_STREAM)


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


def start(ADDR):

    try:
        sock.connect(ADDR)
    except ConnectionRefusedError:
        print("[Errno 111] Connection refused")

    receive_thread = Thread(target=receive)
    receive_thread.start()