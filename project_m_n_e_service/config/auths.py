from ninja.security import HttpBearer
import requests


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        return Auth.authenticate_request(request, token)


class Auth:
    def authenticate_request(request, token: str):
        try:
            if token:
                url = 'http://localhost:8001/authenticate?token='
                return requests.post(url + token)
            raise "Null Token was given"
        except:
            raise "Authentication Connection problems occured"
