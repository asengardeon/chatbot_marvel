# ChatBot Marvel

Projeto da pós graduação em Data Science da FURB para demonstração do uso de chatbots.

Integrantes:
- Cristopher Braatz Cardoso
- Leandro Vilson Battisti
- Lucas Amaral

## Arquitetura

- Rasa 2.5
- MongoDB 4.5

## Dependências

- Docker
- Python 3.8
- Rasa 2.5

## Como executar apenas o Rasa e o MongoDB?

No diretório raiz deste projeto, execute `docker-compose up` para instanciar o MongoDB e o [Mongo Express](http://localhost:8081).

Em seguida, no diretório `rasa-example`, execute `rasa train` (não está sendo commitado o tar.gz) e em seguida `rasa interactive`.

Todas as interações serão salvas na coleção `conversations` na base de dados `rasa`.


## Buildar imagem do actions server

- `docker build -t rasa-marvel:latest .`
- `docker run -p 5055:5055 rasa-marvel`

## Frontend

- Executar `rasa run --enable-api`
- Abrir arquivo `front/index.html` (Por enquanto está com problemas de CORS)