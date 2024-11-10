<h1>PROD Hackaton 2024</h1>

**Версия** `Python 3.12.2`

<h2>1. Создание проекта</h2>

Чтобы скопировать используйте команду

```bash
git clone https://github.com/Alyrineee/prod_backend.git
```

<h2>2. Создание виртуального окружения</h2>
Создайте виртуальное окружение и активируйте его

Для pycharm это делать необязательно
```bash
python3 -m venv venv
source venv/bin/activate
```

<h2>3. Установка зависимостей и создание переменных окружения</h2>

Установите зависимости и скопируйте файл `.env.template`

```bash
pip3 install -r requirements.txt
cp .env.template .env
```

Если необходимо вы можете изменить значения на свои в файле `.env`

`DJANGO_DEBUG` = true/false

`DJANGO_SECRET_KEY` = Ваш ключ (любая строка)

`DJANGO_ALLOWED_HOSTS` = Перечисляется через запятую (если не знаете что писать напишите "*")


<h2>4. Запуск🚀</h2>

```bash
cd ./prod/
python3 manage.py runserver
```
