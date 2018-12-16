# Lazada scrapping

## Build
docker image build . -t lazada_scrape

## Run
docker run -p 8080:8080 -e PYTHONUNBUFFERED=0 lazada_scrape
