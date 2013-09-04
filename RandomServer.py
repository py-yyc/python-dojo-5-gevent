__author__ = 'Jordan Woehr'

import gevent
import random

from flask import Flask
app = Flask('Random')

@app.route('/random')
def handle_random():
    # Sleep for 0-1 seconds
    r = random.random()
    gevent.sleep(r)
    return '%f' % r

def main():
    from gevent.pywsgi import WSGIServer

    s = WSGIServer(('', 45678), app)
    try:
        s.serve_forever()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print('Unexpected exception:', e)
    finally:
        print('Stopping login server...')
        s.stop()

if __name__ == '__main__':
    main()
