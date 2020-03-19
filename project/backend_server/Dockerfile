FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache mariadb-connector-c-dev ;\
    apk add --no-cache --virtual .build-deps \
        build-base \
        mariadb-dev ;\
    pip install mysqlclient;\
    apk del .build-deps 
RUN python -m pip install Django==3.0.3
COPY ./free_chan /free_chan
WORKDIR /free_chan
