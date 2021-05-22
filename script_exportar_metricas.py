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

    csv_columns = ['chat_number', 'total_msg_user_sent', 'texts_sent']

    list_dictionaries = []
    for i, conversation in enumerate(conversations):
        total_messages = 0
        for j, item in conversation.items():
            texts_sent = []
            for dictionary in item:
                for key, value in dictionary.items():
                    if value == 'user':
                        total_messages = total_messages + 1
                    if key == 'text':
                        texts_sent.append(value)

            dictionary = { 'chat_number': i + 1, 'total_msg_user_sent': total_messages, 'texts_sent': texts_sent }
            list_dictionaries.append(dictionary)

    with open("metricas.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in list_dictionaries:
            writer.writerow(data)


if __name__ == "__main__":
    executar()