# ChatBot Marvel

Projeto da pós graduação em Data Science da FURB para demonstração do uso de chatbots.

Integrantes:
- Cristopher Braatz Cardoso
- Leandro Vilson Battisti
- Lucas Amaral

## Arquitetura

- Rasa 2.5
- MongoDB 4.5
- Python 3.8

## Dependências

- Docker ([clique aqui para instalar](https://www.docker.com/products/docker-desktop))
- Caso desejar gerar o modelo NLU, deve ser instalado o Rasa ([clique aqui para instalar](https://rasa.com/))

## Como é a arquitetura do chatbot?

![alt text](https://github.com/asengardeon/chatbot_marvel/blob/main/arquitetura_chatbot_marvel.png)

## Como é o fluxo do chatbot?

![alt text](https://github.com/asengardeon/chatbot_marvel/blob/main/fluxo_conversa_chatbot_mavel.png)

## Como executar o chatbot?

Após instalar o Docker e executá-lo, no diretório raiz deste projeto, execute o comando `docker-compose up`.

Para acessar o frontend, [clique aqui](http://localhost:8000).

Par acessar a base de dados, [clique aqui](http://localhost:8081).

## Como gerar o modelo NLU?

Basta acessar o diretório `./rasa_nlu` e executar `rasa train`

## Como gerar métricas?

Execute no diretório raiz deste projeto `python script_exportar_metricas.py` ou `python3 script_exportar_metricas.py`.

Será salvo o arquivo `metricas.csv` no diretório em questão.

## Como utilizar as métricas para gerar insights?

Com o arquivo gerado, importe-o no notebook do Google Colab [clicando aqui](https://colab.research.google.com/drive/1dHt-hmedM7aH5Em7VCeT6A_JQPxADDZ_?usp=sharing) e execute o notebook inteiro!
