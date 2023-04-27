FROM python:3.10.11-slim-buster
COPY ./src /src
COPY ./requirements.txt /var/requirements.txt
RUN pip install -r /var/requirements.txt
ENV FLASK_APP /src/simple_api/main.py
ENV FLASK_RUN_PORT=80
ENV FLASK_RUN_HOST=0.0.0.0
ENTRYPOINT flask rund