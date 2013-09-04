__author__ = 'Jordan Woehr'

import gevent
from gevent import socket

def handle_client(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            print 'Client closed connection.'
            break
        print 'Received the string \'%s\'. Echoing it back.' % data
        conn.send(data)
    conn.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        gevent.spawn(lambda: handle_client(conn, addr))

if __name__ == '__main__':
    main()
