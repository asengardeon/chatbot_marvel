# -*- coding: utf-8 -*-
"""ChatBot

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dHt-hmedM7aH5Em7VCeT6A_JQPxADDZ_
"""

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Ler CSV
metricas = pd.read_csv('https://raw.githubusercontent.com/asengardeon/chatbot_marvel/main/metricas/metricas.csv', sep = ',', decimal = '.')

# Visualizar os últimos 5 registros para entendimento da estrutura do arquivo
metricas.tail()

# Lista de total de palavras por mensagem enviada por usuário
total_words = []
# Lista com todas as palavras enviadas em todas as mensagens de todos usuários
all_words = []

# Popular as listas acima
for text in metricas.text_sent_by_user:
    total_words.append(len(text.split()))

    words = text.split()
    for word in words:
        all_words.append(word.lower())

# Adicionar coluna com total de palavras da mensagem enviada pelo usuário
metricas['total_words'] = total_words

metricas.tail()

# Total de chats
total_chats = len(metricas.chat_number.unique())
print(total_chats)

# Total de mensagens enviadas
total_texts_sent = len(metricas.chat_number)
print(total_texts_sent)

# Total de palavras enviadas
total_words_sent = len(all_words)
print(total_words_sent)

# Média de mensagens enviadas por chat
average_texts_sent = total_texts_sent / total_chats
print(average_texts_sent)

# Média de palavras enviadas por mensagem
average_words_sent_per_text = total_words_sent / total_texts_sent
print(average_words_sent_per_text)

# Média de palavras enviadas por chat
average_words_sent_per_chat = total_words_sent / total_chats
print(average_words_sent_per_chat)

# Geração de um novo dataframe com base no total de mensagens envidas por usuário por chat
total_texts_sent_per_chat = metricas.groupby('chat_number')['text_sent_by_user'].nunique()

list_total_texts_sent_per_chat = []

chat = 1;
for total in total_texts_sent_per_chat:
    list_total_texts_sent_per_chat.append({'chat_number': chat, 'total_texts_sent_by_user': total})
    chat = chat + 1

df_list_total_texts_sent_per_chat = pd.DataFrame(list_total_texts_sent_per_chat, columns = ['chat_number', 'total_texts_sent_by_user'])

df_list_total_texts_sent_per_chat.tail()

plt.hist(df_list_total_texts_sent_per_chat.total_texts_sent_by_user)
plt.title('Relatório de mensagens enviadas por usuários por chat')
plt.xlabel('Qtde Mensagens')
plt.ylabel('Qtde Chats')
plt.show()

# Gerar top 10 palavras mais frequentes
counts = dict(Counter(all_words).most_common(10))
labels, values = zip(*counts.items())
indSort = np.argsort(values)[::-1]
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]
indexes = np.arange(len(labels))

plt.bar(indexes, values)
plt.xticks(indexes + 0.35, labels)
plt.title('Relatório de top 10 palavras mais enviadas')
plt.xlabel('Palavra')
plt.ylabel('Frequência')
plt.show()

# Ler CSV com votações
votes = pd.read_csv('https://raw.githubusercontent.com/lucamaral/chatbot_marvel/main/metricas/votes.csv', sep = ',', decimal = '.')

# Votação de satisfação
votes.value_counts()

plt.pie(votes.value_counts(), labels = votes.vote.unique())
plt.show()