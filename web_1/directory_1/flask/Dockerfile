# base image
FROM python:3.5.2-alpine

# src dir
ARG project_dir=/web/hello/

ADD requirements.txt $project_dir
ADD hello.py $project_dir
ADD static $project_dir/static/
ADD templates $project_dir/templates/
ADD .secret.txt /secret.txt

# python package install
WORKDIR $project_dir
RUN pip install -r requirements.txt

# container package install
RUN apk update
# RUN apk add vim git etc...
