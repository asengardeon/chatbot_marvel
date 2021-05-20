import string

from google_trans_new import google_translator
from marvel import Marvel

from .config import PUBLIC_KEY, PRIVATE_KEY
import datetime

ITEM_NOT_FOUND = "não encontrado"
m = Marvel(PUBLIC_KEY, PRIVATE_KEY)
t = google_translator()

LIMIT_SEARCH = 100


def __translate_to_english__(text):
  return t.translate(text=text, lang_tgt="en").strip()


def __translate_to_portuguese__(text):
  return t.translate(text=text, lang_tgt="pt").strip()

def char_name(char_name: string):
    found = False
    name = f"Personagem {ITEM_NOT_FOUND}"
    char = m.characters.all(nameStartsWith=__translate_to_english__(char_name))
    if len(char['data']['results']) > 0:
        n = char['data']['results'][0]['name']
        found = True
        name = __translate_to_portuguese__(n)
    return found, name

def char_description(char_name: string):
    found = False
    desc = f"Personagem {ITEM_NOT_FOUND}"
    char = m.characters.all(nameStartsWith=__translate_to_english__(char_name))
    if len(char['data']['results']) > 0:
        c = char['data']['results'][0]['description']
        found = True
        desc = __translate_to_portuguese__(c)
    return found, desc


def char_photo(char_name: string):
    found = False
    result = f"Personagem {ITEM_NOT_FOUND}"
    char = m.characters.all(nameStartsWith=__translate_to_english__(char_name))
    if len(char['data']['results']) > 0:
        resource = char['data']['results'][0]['thumbnail']
        result = f"{resource['path']}/portrait_incredible.{resource['extension']}"
        found = True
    return found, result


def comics_qtd_for_char(char_name: string):
    comics = m.comics.all(title=__translate_to_english__(char_name))
    return str(comics['data']['total'])

def comic_name(comic_name: string):
    found = False
    name = f"Quadrinho {ITEM_NOT_FOUND}"
    comics = m.comics.all(title=__translate_to_english__(comic_name))
    if len(comics['data']['results']) > 0:
        n = comics['data']['results'][0]['title']
        found = True
        name = __translate_to_portuguese__(n)
    return found, name

def date_of_comic(comic: string):
    found = False
    result = f"Quadrinho {ITEM_NOT_FOUND}"
    comics = m.comics.all(title=__translate_to_english__(comic))
    if len(comics['data']['results']) > 0:
        result = comics['data']['results'][0]['dates']
        found = True
    res = ''
    for data in result:
        dat = datetime.datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S-%f").strftime('%d/%m/%Y')
        if data['type'] == 'onsaleDate':
            res += f"Data de venda: {dat} "
        if data['type'] == 'focDate':
            res += f"Data de pré-venda: {dat}"
    return found, res


def creator_of_comic(comic: string):
    found = False
    result = f"Quadrinho {ITEM_NOT_FOUND}"
    comics = m.comics.all(title=__translate_to_english__(comic))
    if len(comics['data']['results']) > 0:
        creators = comics['data']['results'][0]['creators']['items']
        result = ''
        for c in creators:
            result += c['name'] + "\n"
        found = True
    return found, str(result)


def characters_of_comic(comic: string):
    found = False
    result = f"Quadrinho {ITEM_NOT_FOUND}"
    comics = m.comics.all(title=__translate_to_english__(comic))
    if len(comics['data']['results']) > 0:
        characters = comics['data']['results'][0]['characters']['items']
        result = ''
        for c in characters:
            result += c['name'] + "\n"
        found = True
    return found, str(result)


def prices_of_comic(comic: string):
    found = False
    result = f"Quadrinho {ITEM_NOT_FOUND}"
    comics = m.comics.all(title=__translate_to_english__(comic))
    if len(comics['data']['results']) > 0:
        prices = comics['data']['results'][0]['prices']
        result = ''
        for c in prices:
            result += f"{c['price']}\n"
        found = True
    return found, result


def comic_photo(comic: string):
    found = False
    result = f"Quadrinho {ITEM_NOT_FOUND}"
    comics = m.comics.all(title=__translate_to_english__(comic))
    if len(comics['data']['results']) > 0:
        resource = comics['data']['results'][0]['thumbnail']
        result = f"{resource['path']}/portrait_incredible.{resource['extension']}"
        found = True
    return found, result


def comics_of_creator(first_name, last_name):
    found = False
    result = f"Criador {ITEM_NOT_FOUND}"
    creators = m.creators.all(firstName=first_name, lastName=last_name)
    if len(creators['data']['results']) > 0:
        creator_id = creators['data']['results'][0]['id']
        comic_creator = m.creators.comics(creator_id, limit=LIMIT_SEARCH)
        comics = comic_creator['data']['results']
        qtd_max = comic_creator['data']['total']
        result = ''
        actual = 0
        while actual < qtd_max:
            for c in comics:
                result += f"{c['title']}\n"
                actual = actual + 1
            comic_creator = m.creators.comics(creator_id, offset=LIMIT_SEARCH, limit=LIMIT_SEARCH)
            comics = comic_creator['data']['results']
        found = True
    return found, result


def creator_photo(first_name, last_name):
    found = False
    result = f"Criador {ITEM_NOT_FOUND}"
    creators = m.creators.all(firstName=first_name, lastName=last_name)
    if len(creators['data']['results']) > 0:
        resource = creators['data']['results'][0]['thumbnail']
        result = f"{resource['path']}/portrait_incredible.{resource['extension']}"
        found = True
    return found, result
