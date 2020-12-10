# art7 

## introduction

This is one webapp

## Requirements
I making this webapp using Python, Django (python framework for web developer) and The Movie Database API.

For run this project is necessary install:

```
Python = "3.8"
Django = "*"
Pipenv = "*"
```

## Proposta
Este projeto está em construção, tendo isto em mente, enquanto ele se encontrar neste processo irei inserir todas as funcionalidades que pretendo implementar durante o desenvolvimento dele no checklist abaixo para que vocês possam acompanhar o desenvolvimento dele sabendo que funcionalidades irão encontrar.

- [x] Criação e Autenticação de usuários
- [ ] Recuperação de Senhas
- [x] Listas com informações sobre filmes e séries atualizadas de acordo com o The Movie Database
- [x] Pesquisa por filmes ou séries puxando dados do The Movie Database
- [ ] Sistema de lista de filmes e séries
- [ ] Posts sobre filmes e séries

## project structure
O projeto atualmente está com a seguinte estrutura:

```
├── accounts
│   └── migrations
├── art7
├── static
│   ├── css
│   ├── img
│   ├── scss
│   └── vendor
│       ├── bootstrap
│       │   ├── css
│       │   └── js
│       ├── fontawesome-free
│       │   ├── css
│       │   └── webfonts
│       ├── jquery
│       └── simple-line-icons
│           ├── css
│           └── fonts
├── templates
│   └── registration
├── utils
└── webapp
    └── migrations

```

- O diretório raíz do projeto é o `art7/` onde encontraremos as configurações do projeto
- No diretório `webapp/` encontraremos único app do projeto até o momento, ele é responsável pelas funcionalidades da aplicação.
- O diretório `templates/` é onde se encontram os templates html utilizados no projeto
- O diretório `static` é responsável pelos arquivos estáticos do projeto, como css, js, img e etc...


## Run this project
Para rodar este projeto basta possuir todas as ferramentas descritas no tópico <b>Requirements</b> e seguir o seguinte passo a passo:

- 1°: Rode o seguinte comando no diretório do projeto: ```$ pipenv install Pipefile```
- 2°: Ative o seu virtual envairoment com o comando: ```$ pipenv shell``
- 3°: Faça as migrações necessárias para que o banco de dados funcione corretamente com o comando: ```$ python manage.py makemigrations```
- 4°: Migre o conteúdo para o banco de dados executando: ```$ python manage.py migrate```
- 5°: Rode o projeto executando: ```$ python manage.py runserver```
- 6°: Acesse http://localhost:8000/

## Test this project
Para executar os testes desta aplicação basta digitar o seguinte comando no diretório principal do projeto:

```
$ python manage.py test
```




