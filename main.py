from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

def print_hi(name):
    print(f'Hi, {name}')


@app.route('/')
def root():
    return 'Chatbot Marvel'

if __name__ == '__main__':
    print('Serving on 8088...')
    WSGIServer(('127.0.0.1', 8088), app).serve_forever()

