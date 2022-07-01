from ninja.security import HttpBearer
import requests
from config.settings import AUTH_URL as auth_url


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        return Auth.authenticate_request(request, token)


class Auth:
    def authenticate_request(request, token: str):
        try:
            if token:
                return requests.post(auth_url + token)
            raise "Null Token was given"
        except:
            raise "Authentication Connection problems occured"
