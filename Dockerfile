FROM python:3.10.9-slim

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app ./app

CMD [ "python3", "-m", "app.main"]