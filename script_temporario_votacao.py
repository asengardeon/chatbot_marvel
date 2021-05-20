#!/usr/bin/env python

try:
    from pymongo import MongoClient
except:
    print('Dependencias nao instaladas')
    exit(1)


mongo_host = '127.0.0.1'
mongo_port = '27017'
mongo_user = 'rasa'
mongo_password = 'rasa'
mongo_args = '?authSource=admin&ssl=false'
mongo_db_name = 'rasa'
mongo_collection = 'conversations'

def salvar_votacao(id, votacao: int):
    mongo_connection_string = f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/{mongo_args}'

    mongo_client = MongoClient(mongo_connection_string)

    db = mongo_client[mongo_db_name]

    target_collection = db[mongo_collection]

    target_collection.update({'_id': id}, {"$set": {"events.event.votacao": votacao}}

    mongo_client.close()