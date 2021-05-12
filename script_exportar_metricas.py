#!/usr/bin/env python

try:
    from pymongo import MongoClient
    import json
    import pika
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
mongo_query = {'events.event': 'user'}
mongo_project = {"_id" : 1, "events.event" : 1, "events.text" : 1}


def executar():
    mongo_connection_string = f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/{mongo_args}'

    mongo_client = MongoClient(mongo_connection_string)

    db = mongo_client[mongo_db_name]

    target_collection = db[mongo_collection]

    conversations = target_collection.find(mongo_query, mongo_project)

    for i, item in enumerate(conversations):
        print(item)
        print()

    mongo_client.close()


if __name__ == "__main__":
    executar()