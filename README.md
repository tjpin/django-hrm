
# ♻️ Django HR Management

![Alt text](/django-hrm.png "Django HRM")

## ♻️️ About Django-HRM
This's a simple hr management system created as a side project writen in python Django. Feel free to experiment and add additional features if you like.

## 🟢 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.


### Installing

A step by step series of examples that tell you how to get a development env running.

+ Clone repository

```
git clone https://github.com/tjpin/django-hrm.git
```

+ Create a virtual enviroment


```
python -m venv <venv-name>
```

+ Activate virtual enviroment.

git bash windows
```
source <venv-name>/Scripts/activate
```
cmd windows
```
source <venv-name>\Scripts\activate
```
POSIX
```
source <venv-name>/bin/activate
```
#### Run project.
```
cd django-hrm
```
```
python -m pip install -r requirements.txt
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
#### Start server
```
python manage.py runserver
```
##### Important Note.
..................
 >Note this project is configured with redis cache backend.
 >To run without errors, open <strong> settings.py line 127</strong>, either run redis docker with default port 6379.
 >or uncomment Database backend and comment redis backend.
 >Else comment redis backend and configure diffrent backend.
 
 ### Database
 >This project is using default sqlite database which requires no extra setup but its also configured to use postgressql. If you already have postgressql running, comment default database backend and uncomment postgress backend and its configurations. Also remember to create .env file and setup postgress connection creds.
 
## 🔧 Running the tests 

```
python manage.py test
```
or specific app
```
python manage.py test src.<app>
```

### Example: Test staff app
```
python manage.py test src.staff
```

## ⛏️ Technologies used
- [Django](https://docs.djangoproject.com/en/4.1/)
- [Tailwindcss](https://tailwindcss.com/docs/installation)
- [JQuery | Ajax](https://api.jquery.com/jquery.ajax/)
- [postgressql](https://www.postgresql.org/docs/) 

## ✍️ Author

- [@Lazarus Muya](https://github.com/tjpin) - Idea & Initial work

## 🚀 Deployment 

> Deployed by docker but can be deployed anywhere.



