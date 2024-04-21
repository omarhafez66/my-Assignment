FROM python:alpine

WORKDIR /app

COPY paragraphs.txt /app
COPY Omar_Hafez.py /app

RUN pip install nltk

RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords


CMD ["python","Omar_Hafez.py"]
