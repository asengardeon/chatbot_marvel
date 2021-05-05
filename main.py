import string

from flask import Flask, request
from gevent.pywsgi import WSGIServer
from marvel import Marvel

from config import PUBLIC_KEY, PRIVATE_KEY

app = Flask(__name__)

m = Marvel(PUBLIC_KEY, PRIVATE_KEY)


@app.route('/')
def root():
  m.characters.all()
  return "OK"


@app.route('/char_description/<char_name>')
def char_description(char_name: string):
  char = m.characters.all(nameStartsWith=char_name)
  return char['data']['results'][0]['description']


@app.route('/char_photo/<char_name>')
def char_photo(char_name: string):
  char = m.characters.all(nameStartsWith=char_name)
  resource = char['data']['results'][0]['thumbnail']
  return f"{resource['path']}/portrait_incredible.{resource['extension']}"


@app.route('/comics_qtd_for_char/<char_name>')
def comics_qtd_for_char(char_name: string):
  comics = m.comics.all(title=char_name)
  return str(comics['data']['total'])


@app.route('/date_of_comic/<comic>')
def date_of_comic(comic: string):
  comics = m.comics.all(title=comic)
  return str(comics['data']['results'][0]['dates'])


@app.route('/creator_of_comic/<comic>')
def creator_of_comic(comic: string):
  comics = m.comics.all(title=comic)
  creators = comics['data']['results'][0]['creators']['items']
  result = ''
  for c in creators:
      result += c['name']+";"
  return str(result)


@app.route('/characters_of_comic/<comic>')
def characters_of_comic(comic: string):
  comics = m.comics.all(title=comic)
  characters = comics['data']['results'][0]['characters']['items']
  result = ''
  for c in characters:
      result += c['name']+";"
  return str(result)


@app.route('/prices_of_comic/<comic>')
def prices_of_comic(comic: string):
  comics = m.comics.all(title=comic)
  prices = comics['data']['results'][0]['prices']
  result = ''
  for c in prices:
      result += f"{c['price']};"
  return result


@app.route('/comic_photo/<comic>')
def comic_photo(comic: string):
  comics = m.comics.all(title=comic)
  resource = comics['data']['results'][0]['thumbnail']
  return f"{resource['path']}/portrait_incredible.{resource['extension']}"


@app.route('/comics_of_creator/')
def comics_of_creator():
  params = request.args.to_dict()
  creators = m.creators.all(firstName=params['firstName'], lastName=params['lastName'])
  comics = creators['data']['results'][0]['comics']['items']
  result = ''
  for c in comics:
      result += f"{c['name']};"
  return result


@app.route('/qtd_comics_of_creator/')
def qtd_comics_of_creator():
  params = request.args.to_dict()
  creators = m.creators.all(firstName=params['firstName'], lastName=params['lastName'])
  comics = creators['data']['results'][0]['comics']['available']
  return str(comics)



if __name__ == '__main__':
    print('Serving on 8088...')
    WSGIServer(('127.0.0.1', 8088), app).serve_forever()

