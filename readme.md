# Django REST practice

Для запуска проекта вам нужно:

### 1. Склонить репозиторий по ссылке:
```
git clone https://github.com/FitStreet/django_task_16
```
### 2. Прейти в папку проекта:
```bash
cd django_task_16
```
### 3. Создать файл db_config.py и записать в него Переменную DB_CONFIG со своими данными, как указано в примере ниже:
```python
DB_CONFIG = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Название вашей Базы данных',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'localhost',
        'PORT': 5432
    }
}
```
### 4. Зайти в Postgresql и создать там базу данных(название БД должно совпадать с названием в ссылке из 3 пункта):
```postgresql
CREATE DATABASE "Название вашей Базы данных";
```
### 5. В папке проекта создать виртуальное окружение и активировать его:
```bash
python3 -m venv venv
. venv/bin/activate
```
### 6. Установить все расширения для проекта командой:
```bash
pip install -r req.txt
```
### 7. После установки примените миграции:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
### 8. После миграций запустите сервер командой:
```bash
python3 manage.py runserver
```

# Теперь мы можем протестировать наши запросы через Postman или Thunder Client.

### 1. Запрос на получение всех продуктов.

**_URL_** - http://127.0.0.1:8000/product/get/ <br>
Метод:  **GET** <br>
Пример запроса в Postman <br>
![Пример запроса в Postman](https://i.postimg.cc/MH2gs8zh/2023-12-18-153732.png)

### 2. Запрос на получение одного продукта.

**_URL_** - http://127.0.0.1:8000/product/get/"ID продукта, который хотим получить"/ <br>
Метод:  **GET** <br>
Пример запроса в Postman <br>
![Пример запроса в Postman](https://i.postimg.cc/d32jwbGP/2023-12-18-153956.png)

### 3. Запрос на создание нового продукта.

**_URL_** - http://127.0.0.1:8000/product/create/ <br>
Метод:  **POST**<br>
Пример запроса в Postman <br>
**_`title`_** - строка(_str_) |
**_`price`_** - числовое значение(_int_) |
**_`description`_** - строка(_str_) |
**_`image`_** - прямая ссылка на изображение из интернета(_link_)<br>
![Пример запроса в Postman](https://i.postimg.cc/x8TCzs0W/2023-12-18-153750.png)

### 4. Запрос на полное или частичное обновление продукта(в запросе указываем ID продукта, который хотим обновить)

**_URL_** - http://127.0.0.1:8000/product/update/"ID продукта, который хотим обновить"/<br>
Метод:  **PUT**, **PATCH**<br>
Пример запроса в Postman(можем поменять данные частично или все данные сразу) <br>
![Пример запроса в Postman](https://i.postimg.cc/ydyfnC5p/2023-12-18-153945.png)<br>
![Пример запроса в Postman](https://i.postimg.cc/D0d88BSX/2023-12-18-153928.png)

### 5. Запрос на удаление продукта.

**_URL_** - http://127.0.0.1:8000/product/get/"ID продукта, который хотим удалить"/ <br>
Метод:  **DELETE** <br>
Пример запроса в Postman <br>
![Пример запроса в Postman](https://i.postimg.cc/rsQrwMZ4/2023-12-18-154010.png)