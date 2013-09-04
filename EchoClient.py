__author__ = 'Jordan Woehr'

from gevent import socket

def main():
    s = socket.socket()
    s.connect(('localhost', 80))
    s.send('Hello world!')
    print s.recv(1024)
    s.close()

if __name__ == '__main__':
    main()
