# pull official base image
FROM python:3.7

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONUNBUFFERED 1

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY /code /code


# run gunicorn
# CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT
CMD python manage.py runserver