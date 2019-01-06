# Instructions (Danielle)
1. To initialise server, open terminal and key in the following commands
    a. cd Desktop
    b. cd lazada-master
    c. git pull origin master (to pull in latest updates, else skip this)
    d. docker-compose up
2. To shut down server
    a. in the same terminal press ctrl-z
    b. docker-compose down. (This is important else it will still be running in the background)

# Ecommerce scrapping

Current features (server)
1. Crawl lazada for relevant products based on product Name
2. Crawl lazada for top selling items based on category

Current features (website)
1. Crawl lazada for relevant products based on product Name

Upcoming features (server)
1. Extend above features to shopee and Qoo10

Upcoming features (website)
1. Crawl lazada for top selling items based on category
2. Extend features for lazada to qoo10 and shopee

## Docker Build
### Build
docker image build . -t lazada_scrape

### Run
docker run -p 8080:8080 -e PYTHONUNBUFFERED=0 lazada_scrape

## Non docker Build
1. Install python and git
2. cd to desired directory
3. open cmd prompt in desired directory
4. "git clone https://github.com/woonzh/lazada.github"
5. "cd lazada"
6. "pip install -r requirements.txt (assuming you have directed pip to pip3 for python3)"
7. "python server.py"
8. Open browser and go to "http://localhost:8080"
