# hw_docker

С помощью docker compose и Dockerfile создаются 3 сервиса. Все сервисы находятся в одной docker-сети типа user-defined bridge.

Сервис-1. База данных\
Образ - mariadb\
Название сервиса - db

В БД будут храниться данные для веб-приложения Сервиса-3. Данные представляют собой два столбца\
name (строковый)\
age   (целочисленный)

Сервис-2. Скрипт для заполнения БД

Образ - самодельный\
Название сервиса - filler

Сервис-2 дожидается, пока Сервис-1 запущен и готов принимать подключения, затем к нему по сети и заполняет набором данных.

Сервис-3. Веб-сервер

Образ - самодельный\
Название сервиса - web

Контейнер с веб-сервером, который может отдавать данные из Сервиса-1 по http-запросу.

веб-сервер запускается после Сервиса-1 и Сервиса-2\
веб-сервер соединяется с контейнером БД по сети, делает запрос, получает ответ и отдает данные в http ответе\
веб-сервер умеет принимать следующие http-запросы:\
GET / - возвращает все данные из БД в формате JSON, статус 200\
GET /health - возвращает JSON {"status": "OK"}, статус 200\
остальные запросы - возвращает статус 404\
веб-сервер запускается на порте 8000\
контейнер с веб-сервером имеет проброшенный порт 8000:8000

## Installation

docker: https://docs.docker.com/engine/install/ubuntu/

для исользования docker без sudo прав:

```
$ sudo groupadd docker
```

```
$ sudo usermod -aG docker $USER
```

```
$ newgrp docker
```
## Usage

в терминале:
```
$ docker compose up -d --build
```
для остановки:
```
$ docker rm -f db
```

```
$ docker rm -f filler
```

```
$ docker rm -f web
```

```
$ docker compose down
```
