import requests


class Slack:
    # Classe de integração através do método de webhook
    def __init__(self, url):
        self.url = url
        self.headers = {'Content-Type': 'application/json'}

    def post(self, data):
        res = requests.post(self.url, headers=self.headers, data=data)
        return res.text
