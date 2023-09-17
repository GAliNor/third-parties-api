import requests
import json


class Elasticsearch:

    def __init__(self, host, token=None):
        self.protocol = 'http'
        self.host = host
        self.port = 9200
        self.headers = { 'content-type': 'application/json' }
        if token:
            self.headers['authorization'] = f'Basic {token}'

        self.url = f'{self.protocol}://{self.host}:{self.port}'

    
    def bulk(self, payload):
        target_endpoint = f'{self.url}/_bulk'
        response = requests.post(target_endpoint, headers=self.headers, data=payload)
        return json.loads(response.text)
    

    def create_index(self, index_name, payload = None):
        target = f'{self.url}/{index_name}'
        response = requests.put(target, headers=self.headers, data=json.dumps(payload))
        return json.loads(response.text)
