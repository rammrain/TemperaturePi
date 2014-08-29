import requests


class Sender:
    config = 0

    def __init__(self, config):
        self.config = config

    def send(self, temperature, sensor):
        request_params = {
            'hash': self.config.apiHash,
            'sensor': sensor,
            'temperature': temperature
        }

        r = requests.get(self.config.requestUrl, params=request_params)
