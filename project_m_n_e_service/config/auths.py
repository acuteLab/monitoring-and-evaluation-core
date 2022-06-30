from ninja.security import HttpBearer
import requests


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        return Auth.authenticate_request(request, token)


class Auth:
    def authenticate_request(request, token: str):
        url = 'http://localhost:8001/authenticate?token='
        return requests.post(url + token)
