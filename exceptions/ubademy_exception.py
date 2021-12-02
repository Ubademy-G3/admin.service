class UbademyException(Exception):
    def __init__(self, status_code, detail):
        super().__init__(detail)
        self.detail = detail
        self.status_code = status_code


class InvalidMicroserviceStateException(UbademyException):
    def __init__(self, detail):
        msg = f"Microsercice has an invalid state: \"{detail}\". Expected values: are \"active\", \"blocked\" and \"blocked\""
        super().__init__(status_code=400, detail=msg)
