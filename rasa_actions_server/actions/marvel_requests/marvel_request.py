import os
import string

from google_trans_new import google_translator
from marvel import Marvel
import pickle


from .config import PUBLIC_KEY, PRIVATE_KEY
import datetime
from rapidfuzz import process, fuzz

import logging



ITEM_NOT_FOUND = "não encontrado"
m = Marvel(PUBLIC_KEY, PRIVATE_KEY)
t = google_translator()

LIMIT_SEARCH = 100


only_load_cache = True

def __first_valid_comic_id_from_list(comic_list_tuple, comics_ids):
    for comic in comic_list_tuple:
        nome, percentual, pos = comic
        comics = m.comics.get(comics_ids[pos])
        if len(comics['data']['results']) > 0:
            return comics_ids[pos]
    nome, percentual, pos = comic_list_tuple[-1]
    return comics_ids[pos]

def __files_cache_exists(file_name):
    full_file = f"{os.path.dirname(os.path.abspath(__file__))}{os.path.sep}{file_name}"
    return os.path.isfile(full_file)

def __save_list_to_file(file_name, list):
    full_file = f"{os.path.dirname(os.path.abspath(__file__))}{os.path.sep}{file_name}"
    with open(full_file, 'wb') as fp:
        pickle.dump(list, fp)


def __load_list_from_file(file_name):
    full_file = f"{os.path.dirname(os.path.abspath(__file__))}{os.path.sep}{file_name}"
    with open(full_file, 'rb') as fp:
        list = pickle.load(fp)
    return list


def __load_all_heroes_names():
    logging.info("Iniciando carrregamento de herois")
    list_heroes_names = []
    if only_load_cache or __files_cache_exists('heroes.names'):
        list_heroes_names = __load_list_from_file('heroes.names')
    else:
        chars = m.characters.all(limit=LIMIT_SEARCH)
        if len(chars['data']['results']) > 0:
            qtd_max = chars['data']['total']
            actual = 0
            while actual < qtd_max:
                for c in chars['data']['results']:
                    list_heroes_names.append(c['name'])
                    actual = actual + 1
                chars = m.characters.all(offset=actual, limit=LIMIT_SEARCH)
        __save_list_to_file('heroes.names', list_heroes_names)
    return list_heroes_names
    logging.info(f"Concluido carrregamento de herois com {len(list_heroes_names)} herois")


def __load_from_offset(list, list_ids, offset=0):
    list_comics_names = list
    list_comics_ids = list_ids
    comics = m.comics.all(offset=offset, limit=LIMIT_SEARCH)
    if len(comics['data']['results']) > 0:
        qtd_max = comics['data']['total']
        actual = offset
        while actual < qtd_max:
            for c in comics['data']['results']:
                list_comics_names.append(c['title'])
                list_comics_ids.append(c['id'])
                actual = actual + 1
            comics = m.comics.all(offset=actual, limit=LIMIT_SEARCH)
            __save_list_to_file('comics.names', list_comics_names)
            __save_list_to_file('comics.ids', list_comics_ids)
            __save_list_to_file('comic.offset', [qtd_max, actual])
    return list_comics_names, list_comics_ids


def __load_all_comic_names():
    logging.info("Iniciando carrregamento de quadrinhos")
    list_comics_names = []
    list_comics_ids = []
    if only_load_cache or (__files_cache_exists('comics.names') and __files_cache_exists('comic.offset')):
        list = __load_list_from_file('comics.names')
        list_ids = __load_list_from_file('comics.ids')
        offs = __load_list_from_file('comic.offset')
        if len(list) != offs[0] or len(list) == 0:
            list_comics_names, list_comics_ids = __load_from_offset(list, list_ids, offs[1])
    else:
        list_comics_names, list_comics_ids = __load_from_offset(list_comics_names, list_comics_ids)

    logging.info(f"Concluido carrregamento de quadrinhos, com {len(list_comics_names)} quadrinhos")

    return list_comics_names, list_comics_ids



__load_all_comic_names()
__load_all_heroes_names()



def __fix_char_name(char_name: str):
  hero_names = __load_all_heroes_names()
  logging.info(process.extractOne(char_name, hero_names, scorer=fuzz.WRatio))
  nome, percentual, id = process.extractOne(char_name, hero_names, scorer=fuzz.WRatio)
  return nome


def __get_id_from_comic_name(comic_name: str):
  comic_names, comics_ids = __load_all_comic_names()
  logging.info(process.extract(comic_name, comic_names, scorer=fuzz.WRatio))
  comics = process.extract(comic_name, comic_names, scorer=fuzz.WRatio)
  id = __first_valid_comic_id_from_list(comics, comics_ids)
  return id


def __translate_char_name_to_english(char_name):
    __load_all_heroes_names()
    return __fix_char_name(__translate_to_english__(char_name))


def __translate_to_english__(text):
  return t.translate(text=text, lang_tgt="en").strip()


def __translate_to_portuguese__(text):
  return t.translate(text=text, lang_tgt="pt").strip()


def char_name(char_name: string):
    found = False
    name = f"Personagem {ITEM_NOT_FOUND}"
    char = m.characters.all(nameStartsWith=__translate_char_name_to_english(char_name))
    if len(char['data']['results']) > 0:
        n = char['data']['results'][0]['name']
        found = True
        name = __translate_to_portuguese__(n)
    return found, name


def char_description(char_name: string):
    found = False
    desc = f"Personagem {ITEM_NOT_FOUND}"
    char = m.characters.all(nameStartsWith=__translate_char_name_to_english(char_name))
    if len(char['data']['results']) > 0:
        c = char['data']['results'][0]['description']
        found = True
        desc = __translate_to_portuguese__(c)
    return found, desc


def char_photo(char_name: string):
    found = False
    result = f"Personagem {ITEM_NOT_FOUND}"
    char = m.characters.all(nameStartsWith=__translate_char_name_to_english(char_name))
    if len(char['data']['results']) > 0:
        resource = char['data']['results'][0]['thumbnail']
        result = f"{resource['path']}/portrait_incredible.{resource['extension']}"
        found = True
    return found, result


def comics_qtd_for_char(char_name: string):
    comics = m.comics.all(title=__translate_char_name_to_english(char_name))
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
    comics = m.comics.get(__get_id_from_comic_name(comic))
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
    comics = m.comics.get(__get_id_from_comic_name(comic))
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
    comics = m.comics.get(__get_id_from_comic_name(comic))
    if len(comics['data']['results']) > 0:
        characters = comics['data']['results'][0]['characters']['items']
        result = ''
        for c in characters:
            result += c['name'] + "\n"
        found = True
    return found, str(result)


if __name__ == 'marvel_request':
    __load_all_heroes_names()

def prices_of_comic(comic: string):
    found = False
    result = f"Quadrinho {ITEM_NOT_FOUND}"
    comics = m.comics.get(__get_id_from_comic_name(comic))
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
    comics = m.comics.get(__get_id_from_comic_name(comic))
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
            comic_creator = m.creators.comics(creator_id, offset=actual, limit=LIMIT_SEARCH)
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
