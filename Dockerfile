# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

LABEL maintainer="lord pangan <lord.pangan@gmail.com>" \
  description="visitor counter app" \
  org.label-schema.vcs-url="git@github.com:lordpangan/berkeley-project.git"

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV REDIS_HOST='0.0.0.0' \
    REDIS_PORT=6379 \
    REDIS_PASS='changeme'

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]