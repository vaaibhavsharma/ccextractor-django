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
DEBUG=True
SECRET_KEY= # Put your Django project secret key here - keep it secret!
RECAPTCHA_PUBLIC_KEY= # Add your reCAPTCHA site key here
RECAPTCHA_PRIVATE_KEY= # Add your reCAPTCHA private key here - keep it secret too!
environment= (prod for production and dev for developement)
# Still in work (for amazon rds)
DB_NAME=
HOST=
PASSWORD=
```

### Django Configurations

```sh
python manage.py makemigrations userProfile quiz
python manage.py migrate
python manage.py runserver 8080
```

Your local instance will now be up and running at http://127.0.0.1:8080/
