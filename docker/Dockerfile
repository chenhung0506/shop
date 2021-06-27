FROM python:3.7-alpine AS base
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./app/requirements.txt /usr/src/app
RUN apk update && apk add --virtual .py_deps build-base python3-dev libffi-dev gcc musl-dev openssl-dev
RUN pip install -r /usr/src/app/requirements.txt
RUN apk del .py_deps &&\
    apk add -U tzdata &&\
    apk add curl &&\
    echo "Asia/Taipei" > /etc/timezone
COPY ./app /usr/src/app
CMD ["python", "manage.py", "runserver"]
