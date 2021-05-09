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

- Docker ([clique aqui para instalar](https://www.docker.com/products/docker-desktop)

## Como executar o chatbot?

Após instalar o Docker e executá-lo, no diretório raiz deste projeto, execute o comando `docker-compose up`.

Para acessar o frontend, [clique aqui](http://localhost:8000).

Par acessar a base de dados, [clique aqui](http://localhost:8081).

## TODO incluir no docker-compose

- Na pasta chatbot_marvel/rasa_nlu, executar:
- `rasa run --enable-api --cors ['http://localhost:8000']`
- Na pasta chatbot_marvel/front, executar:
- `python -m http.server`