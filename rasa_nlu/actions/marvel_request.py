import string
from urllib import request
from marvel import Marvel
from .config import PUBLIC_KEY, PRIVATE_KEY
from google_trans_new import google_translator

m = Marvel(PUBLIC_KEY, PRIVATE_KEY)
t = google_translator()

LIMIT_SEARCH = 100

def char_description(char_name: string):
  char = m.characters.all(nameStartsWith=char_name)
  c = char['data']['results'][0]['description']
  return t.translate(text=c, lang_tgt="pt")


def char_photo(char_name: string):
  char = m.characters.all(nameStartsWith=char_name)
  resource = char['data']['results'][0]['thumbnail']
  return f"{resource['path']}/portrait_incredible.{resource['extension']}"


def comics_qtd_for_char(char_name: string):
  comics = m.comics.all(title=char_name)
  return str(comics['data']['total'])


def date_of_comic(comic: string):
  comics = m.comics.all(title=comic)
  return str(comics['data']['results'][0]['dates'])


def creator_of_comic(comic: string):
  comics = m.comics.all(title=comic)
  creators = comics['data']['results'][0]['creators']['items']
  result = ''
  for c in creators:
      result += c['name']+";"
  return str(result)


def characters_of_comic(comic: string):
  comics = m.comics.all(title=comic)
  characters = comics['data']['results'][0]['characters']['items']
  result = ''
  for c in characters:
      result += c['name']+";"
  return str(result)


def prices_of_comic(comic: string):
  comics = m.comics.all(title=comic)
  prices = comics['data']['results'][0]['prices']
  result = ''
  for c in prices:
      result += f"{c['price']};"
  return result


def comic_photo(comic: string):
  comics = m.comics.all(title=comic)
  resource = comics['data']['results'][0]['thumbnail']
  return f"{resource['path']}/portrait_incredible.{resource['extension']}"


def comics_of_creator():
  params = request.args.to_dict()
  creators = m.creators.all(firstName=params['firstName'], lastName=params['lastName'])
  creator_id = creators['data']['results'][0]['id']
  comic_creator = m.creators.comics(creator_id, limit=LIMIT_SEARCH)
  comics = comic_creator['data']['results']
  qtd_max = comic_creator['data']['total']
  result = ''
  actual = 0;
  while(actual < qtd_max):
    for c in comics:
        result += f"{c['title']};"
        actual = actual + 1
    comic_creator = m.creators.comics(creator_id, offset=LIMIT_SEARCH, limit=LIMIT_SEARCH)
    comics = comic_creator['data']['results']
  return result


def qtd_comics_of_creator():
  params = request.args.to_dict()
  creators = m.creators.all(firstName=params['firstName'], lastName=params['lastName'])
  comics = creators['data']['results'][0]['comics']['available']
  return str(comics)
