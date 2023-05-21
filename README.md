### Django-FASTAPI

Simple CRUD APIs with FASTAPI


## Setup

```
virtualenv venv
pip install -r requirements.txt
cd django_fastapi/
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser 
```

## Running

```
uvicorn project.asgi:app --debug
```

## Routes

The Django app is available at `/django` (e.g. `http://localhost:8000/django/admin/)`

The FastAPI app is is available at `/api` (e.g. `http://localhost:8000/api/items/)`

## FASTAPI Docs

'http://localhost:8000/docs'
