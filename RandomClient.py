__author__ = 'Jordan Woehr'

import gevent
from gevent import monkey
monkey.patch_socket()

import urllib2

def get_random_number():
    req = urllib2.urlopen(
        'http://localhost:45678/random'
    )
    num = float(req.read())
    print num

def main():
    g = [gevent.spawn(get_random_number) for i in range(100)]
    gevent.joinall(g)

if __name__ == '__main__':
    main()
