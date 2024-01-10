FROM python:3.12.1-alpine3.19 as devel
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN apk add libc-dev libffi-dev gcc bash

COPY ./requirements.txt  .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]

COPY . .
