# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY .env .env
RUN pip3 install --no-cache-dir -r requirements.txt
RUN python3 -m spacy download en_core_web_lg
RUN python3 -m nltk.downloader stopwords

COPY . .

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
