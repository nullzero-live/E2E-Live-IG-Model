'''A python client for Elasticsearch Service: 

- API Key is stored in a .env file

'''

import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

CLOUD_ID = "elastic-logging:YXVzdHJhbGlhLXNvdXRoZWFzdDEuZ2NwLmVsYXN0aWMtY2xvdWQuY29tJGZkNTZmYjIxZTkzNzQxYzg5YjM5ZmIzNzlhZDJlNTc4JGU4YjFjMzVmMTRmZjRlODFiOWJjNDQ2ZThjOThiMzUw"
API_KEY = os.getenv("ES_API_KEY")

# Create the client instance
client = Elasticsearch(
    cloud_id=CLOUD_ID,
    api_key=API_KEY,
)


          