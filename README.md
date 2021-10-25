# «API для Yatube»
## **Описание**
Данный проект создан для предоставления API к моей соцсети, в которой каждый может поделиться каким-то интересным постом, подписаться на классного автора, почитать посты из интересующей группы или даже оставить свой комментарий.
## **Установка**
* Клонируйте репозиторий
>  < https://github.com/ainokyn/api_final_yatube.git > 

* Cоздайте и активируйте виртуальное окружение:
> < python -m venv venv> 
> < source venv/Scripts/activate> 

* Установить зависимости из файла requirements.txt:
> < pip install -r requirements.txt> 

* Выполнить миграции:
> python manage.py migrate

* Запустить проект:
> python3 manage.py runserver

## **Примеры**
- Запросы GET
<url = "http://127.0.0.1:8000/api/v1/posts/8"> 
<{
    "id": 8,
    "author": "user1",
    "text": "r",
    "pub_date": "2021-10-22T22:16:00.576460Z",
    "image": null,
    "group": null
}>
Responses: 200
<url = "http://127.0.0.1:8000/api/v1/posts/"> 
<[
    {
        "id": 8,
        "author": "user1",
        "text": "r",
        "pub_date": "2021-10-22T22:16:00.576460Z",
        "image": null,
        "group": null
    },
    {
        "id": 9,
        "author": "user1",
        "text": "user111111",
        "pub_date": "2021-10-22T22:16:07.931584Z",
        "image": null,
        "group": null
    }
]>
Responses: 200, 400, 401

- Запросы POST
Request samples:
<{
    "text": "text"
}>
Response samples:
<{
    "id": 10,
    "author": "user1",
    "text": "text",
    "pub_date": "2021-10-25T20:46:13.059333Z",
    "image": null,
    "group": null
}>
Responses: 200, 400, 401

- Запросы PUT
Request samples:
<{
    "text": "text1"
}>
Response samples: 
<{
    "id": 10,
    "author": "user1",
    "text": "text1",
    "pub_date": "2021-10-25T20:46:13.059333Z",
    "image": null,
    "group": null
}>
Responses: 200, 400, 401, 403, 404

- Запросы PATCH
Request samples:
<{
    "text": "text2"
}>
Response samples:
<{
    "id": 10,
    "author": "user1",
    "text": "text2",
    "pub_date": "2021-10-25T20:46:13.059333Z",
    "image": null,
    "group": null
}>
Responses: 200, 401, 403, 404