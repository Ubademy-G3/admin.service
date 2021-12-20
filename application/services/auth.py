import os
from dotenv import load_dotenv
from exceptions.auth_exception import ApiKeyException
import logging

logger = logging.getLogger(__name__)

load_dotenv()


class AuthService:
    def __init__(self):

        self.api_key = os.getenv("API_KEY")

    def check_api_key(self, api_key):

        if api_key == self.api_key:
            return True
        logger.warning("Api key %s is not valid", api_key)
        raise ApiKeyException()


auth_service = AuthService()
