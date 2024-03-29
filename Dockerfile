FROM python:3.10-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .
COPY embed .
COPY burritoman.jpg .
COPY rockwoman.jpg .

ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=8080"]

