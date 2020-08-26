FROM python:3.6

ARG PROJECT_HOME=/usr/local/covid19_data

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR ${PROJECT_HOME}
COPY ./database /database
COPY ./src /src