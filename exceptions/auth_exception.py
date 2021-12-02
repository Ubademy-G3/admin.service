class AuthorizationException(Exception):
    def __init__(self, status_code, detail):
        super().__init__(detail)
        self.detail = detail
        self.status_code = status_code


class ApiKeyException(AuthorizationException):
    def __init__(self):
        msg = "Exception with API Key"
        super().__init__(status_code=401, detail=msg)
