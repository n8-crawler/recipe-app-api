FROM python:3.9-alpine3.13
LABEL maintainers="nightcrawler1995.com"
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN    python -m venv /py
RUN    /py/bin/pip install --upgrade pip
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev
RUN    /py/bin/pip install -r /tmp/requirements.txt
RUN    rm -rf /tmp
RUN apk del .tmp-build-deps
RUN    adduser \
            --disabled-password\
            --no-create-home\
            django-user

ENV PATH="/py/bin:$PATH"
USER django-user
