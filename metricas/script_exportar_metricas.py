#!/usr/bin/env python

try:
    from pymongo import MongoClient
    import csv
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
mongo_project = {'_id': 0, 'events.event': 1, 'events.text': 1}


def executar():
    mongo_connection_string = f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/{mongo_args}'

    mongo_client = MongoClient(mongo_connection_string)

    db = mongo_client[mongo_db_name]

    target_collection = db[mongo_collection]

    conversations = target_collection.find(mongo_query, mongo_project)

    mongo_client.close()

    csv_columns = ['chat_number', 'text_sent_by_user']

    list_dictionaries = []
    for i, conversation in enumerate(conversations):
        total_messages = 0
        for j, item in conversation.items():
            texts_sent = []
            for dictionary in item:
                isUser = False
                for key, value in dictionary.items():
                    if value == 'user':
                        isUser = True
                    if key == 'text' and isUser == True:
                        list_dictionaries.append({ 'chat_number': i + 1, 'text_sent_by_user': value})

    with open("metricas.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in list_dictionaries:
            writer.writerow(data)

def exportar_votacoes():
    mongo_connection_string = f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/{mongo_args}'

    mongo_client = MongoClient(mongo_connection_string)

    db = mongo_client[mongo_db_name]

    target_collection = db['votes']

    votes = target_collection.find({}, {'vote' : 1})

    mongo_client.close()

    csv_columns = ['vote']

    list_dictionaries = []
    for i, vote in enumerate(votes):
        list_dictionaries.append({'vote': vote['vote']})

    with open("votes.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in list_dictionaries:
            writer.writerow(data)

if __name__ == "__main__":
    executar()
    exportar_votacoes()