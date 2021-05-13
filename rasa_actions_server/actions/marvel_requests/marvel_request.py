import string

from google_trans_new import google_translator
from marvel import Marvel

from .config import PUBLIC_KEY, PRIVATE_KEY

ITEM_NOT_FOUND = "não encontrado"
m = Marvel(PUBLIC_KEY, PRIVATE_KEY)
t = google_translator()

LIMIT_SEARCH = 100


def char_description(char_name: string):
    found = False
    desc = f"Personagem {ITEM_NOT_FOUND}"
    char = m.characters.all(nameStartsWith=char_name)
    if len(char['data']['results']) > 0:
        c = char['data']['results'][0]['description']
        found = True
        desc = t.translate(text=c, lang_tgt="pt")
    return found, desc


def char_photo(char_name: string):
    found = False
    result = f"Personagem {ITEM_NOT_FOUND}"
    char = m.characters.all(nameStartsWith=char_name)
    if len(char['data']['results']) > 0:
        resource = char['data']['results'][0]['thumbnail']
        result = f"{resource['path']}/portrait_incredible.{resource['extension']}"
        found = True
    return found, result


def comics_qtd_for_char(char_name: string):
    comics = m.comics.all(title=char_name)
    return str(comics['data']['total'])


def date_of_comic(comic: string):
    found = False
    result = f"Quadrinho {ITEM_NOT_FOUND}"
    comics = m.comics.all(title=comic)
    if len(comics['data']['results']) > 0:
        result = str(comics['data']['results'][0]['dates'])
        found = True
    return found, result


def creator_of_comic(comic: string):
    found = False
    result = f"Quadrinho {ITEM_NOT_FOUND}"
    comics = m.comics.all(title=comic)
    if len(comics['data']['results']) > 0:
        creators = comics['data']['results'][0]['creators']['items']
        result = ''
        for c in creators:
            result += c['name'] + ";"
        found = True
    return found, str(result)


def characters_of_comic(comic: string):
    found = False
    result = f"Quadrinho {ITEM_NOT_FOUND}"
    comics = m.comics.all(title=comic)
    if len(comics['data']['results']) > 0:
        characters = comics['data']['results'][0]['characters']['items']
        result = ''
        for c in characters:
            result += c['name'] + ";"
        found = True
    return found, str(result)


def prices_of_comic(comic: string):
    found = False
    result = f"Quadrinho {ITEM_NOT_FOUND}"
    comics = m.comics.all(title=comic)
    if len(comics['data']['results']) > 0:
        prices = comics['data']['results'][0]['prices']
        result = ''
        for c in prices:
            result += f"{c['price']};"
        found = True
    return found, result


def comic_photo(comic: string):
    found = False
    result = f"Quadrinho {ITEM_NOT_FOUND}"
    comics = m.comics.all(title=comic)
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
                result += f"{c['title']};"
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
