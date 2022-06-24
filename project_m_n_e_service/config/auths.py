from ninja.security import HttpBearer


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        return Auth.authenticate_request(request, token)


class Auth:
    def authenticate_request(request, token: str):
        pass
