FROM python:3.6.7-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

ENV Name lazada_scrape

CMD ["python", "server.py"]
