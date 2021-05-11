import string

from flask import Flask, request
from gevent.pywsgi import WSGIServer
from marvel import Marvel
from google_trans_new import google_translator
from rasa_actions_server.actions.marvel_requests.config import PUBLIC_KEY, PRIVATE_KEY
from rasa_actions_server.actions.marvel_requests import marvel_request

ITEM_NOT_FOUND = "não encontrado"

app = Flask(__name__)

m = Marvel(PUBLIC_KEY, PRIVATE_KEY)
t = google_translator()

LIMIT_SEARCH = 100


@app.route('/')
def root():
    m.characters.all()
    return "OK"


@app.route('/char_description/<char_name>')
def char_description(char_name: string):
    found, desc = marvel_request.char_description(char_name)
    return desc


@app.route('/char_photo/<char_name>')
def char_photo(char_name: string):
    found, result = marvel_request.char_photo(char_name)
    return result


@app.route('/comics_qtd_for_char/<char_name>')
def comics_qtd_for_char(char_name: string):
    result = marvel_request.comics_qtd_for_char(char_name)
    return result


@app.route('/date_of_comic/<comic>')
def date_of_comic(comic: string):
    found, result = marvel_request.date_of_comic(comic)
    return result


@app.route('/creator_of_comic/<comic>')
def creator_of_comic(comic: string):
    found, result = marvel_request.creator_of_comic(comic)
    return result


@app.route('/characters_of_comic/<comic>')
def characters_of_comic(comic: string):
    found, result = marvel_request.characters_of_comic(comic)
    return result


@app.route('/prices_of_comic/<comic>')
def prices_of_comic(comic: string):
    found, result = marvel_request.prices_of_comic(comic)
    return result


@app.route('/comic_photo/<comic>')
def comic_photo(comic: string):
    found, result = marvel_request.comic_photo(comic)
    return result


@app.route('/comics_of_creator/')
def comics_of_creator():
    params = request.args.to_dict()
    first_name = params['firstName']
    last_name = params['lastName']
    found, result = marvel_request.comics_of_creator(first_name, last_name)
    return result


@app.route('/qtd_comics_of_creator/')
def qtd_comics_of_creator():
    params = request.args.to_dict()
    first_name = params['firstName']
    last_name = params['lastName']
    found, result = marvel_request.qtd_comics_of_creator(first_name, last_name)
    return result


if __name__ == '__main__':
    print('Serving on 8088...')
    WSGIServer(('127.0.0.1', 8088), app).serve_forever()
