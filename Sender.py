import requests


class Sender:
    config = 0

    def send(self, temperature, sensor):
        request_params = {
            'sensor': sensor,
            'temperature': temperature
        }

        return requests.post('http://webser.ee:3000/temperature', request_params)
