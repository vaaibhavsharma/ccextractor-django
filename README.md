# ccextractor-django

### First Steps

```sh
git clone https://github.com/vaaibhavsharma/ccextractor-django.git
cd ccextractor-django
python3 -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

### Environment Variables

Make file .env inside simpleQuiz2 with following content

```sh
DEBUG=
SECRET_KEY=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
```

### Django Configurations

```sh
python manage.py makemigrations videobasic
python manage.py migrate
python manage.py runserver 8080
```

### Django Celery Configurations

- Open new terminal with same virtual environment 
```sh
celery -A videoshare worker --pool=solo -l INFO
```


Your local instance will now be up and running at http://127.0.0.1:8080/
