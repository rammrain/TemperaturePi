import requests
from Config import *

class Sender:
    config = 0

    def __init__(self, config):
        self.config = config

    def send(self, temperature, sensor):
        requestParams = {
            'hash': self.config.apiHash,
            'sensor': sensor,
            'temperature': temperature
        }
        
        return requests.get(self.config.requestUrl, params=requestParams)

