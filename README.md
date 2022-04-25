# Fake Identity Information Generator

## Задание

*Написать API, который отдаёт по HTTP запросу с параметрами список сгенерированных случайным образом персон.*



__Данные о персоне:__

1. Фамилия
2. Имя
3. Дата рождения
4. Логин
5. Пароль


*Пример:*

1. Ощепков
2. Иван
3. 24.11.1988
4. fuzz88
5. xDdfD@sqa21e



__Параметры запроса:__

1. Пол (Мужской, Женский, Оба)
2. Возраст (Диапазон от и до)
3. Количество персон

*Пример:*

GET /persons?gender=0&start_age=18&end_age=70&count=100


### Cтэк

python 3.10, requests, fastapi, sqlite3, docker, docker-compose

Для управления зависимостями используйте pip и pip-tools.


### Инструкция

Управление зависимостями (при запуске выполнять не нужно):
```
pip install pip-tools  # установить pip-tools
pip-compile            # создать requirements.txt на основе requirements.in
```

Запуск:
```
docker-compose up
```