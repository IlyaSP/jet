FROM python:3.7.2-alpine3.8


WORKDIR /home/app
COPY ping.py /home/app

ENTRYPOINT ["python3", "/home/app/ping.py"]
