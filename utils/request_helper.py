import requests


class APIRequest:
    @staticmethod
    def send_get(url):
        return requests.get(url)

    @staticmethod
    def send_post(url, data):
        return requests.post(url, json=data)

    @staticmethod
    def send_put(url, data):
        return requests.put(url, json=data)

    @staticmethod
    def send_delete(url):
        return requests.delete(url)
