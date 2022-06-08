FROM python:3.6

WORKDIR '/app'

ENV FLASK_APP = app.py


COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .



CMD [ "python", "app.py"]