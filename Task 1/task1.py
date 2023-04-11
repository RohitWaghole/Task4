import pymongo
import requests
import json

# MongoDB Connection
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['data']
collection = db['github']


# Fetch data from github's rest api and storing it in mongodb
def fetch_and_store_data(endpoint, collection,user,repo):
    response = requests.get(endpoint.format(user=user, repo=repo, path=path))
    data = json.loads(response.text)
    for item in data:
        # if its a file then only store the data
        if item['type'] == 'file':
            file_content = requests.get(item['download_url']).text
            with open(item['name'], 'wb') as f:
                f.write(file_content.encode('utf-8'))

            # saving the data into mongodb
            with open(item['name'], 'rb') as f:
                file_content = f.read().decode('utf-8')
                file_data = {
                    'name': item['name'],
                    'content': file_content,
                    'path': item['path'],
                    'url': item['url']
                }
                collection.insert_one(file_data)


endpoint = 'https://api.github.com/repos/{user}/{repo}/contents/{path}'
user = 'RohitWaghole'
repo = 'Assignment-2'
path = ''

fetch_and_store_data(endpoint,collection,user,repo)
