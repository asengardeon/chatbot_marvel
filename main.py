import string

from flask import Flask
from gevent.pywsgi import WSGIServer
from marvel import Marvel

app = Flask(__name__)
PUBLIC_KEY = ""
PRIVATE_KEY = ""

m = Marvel(PUBLIC_KEY, PRIVATE_KEY)


@app.route('/')
def root():
  m.characters.all()
  return "OK"


@app.route('/char_description/<char_name>')
def char_description(char_name: string):
  char = m.characters.all(nameStartsWith=char_name)
  return char['data']['results'][0]['description']


if __name__ == '__main__':
    print('Serving on 8088...')
    WSGIServer(('127.0.0.1', 8088), app).serve_forever()

