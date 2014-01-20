import requests
import Config

class Sender:
    config = 0

    def __init__(self, config):
        self.config = config

    def send(self, temperature, sensor):
        print("aaaa")
                 
