import requests

from .exceptions import *

LINE_API_URL = 'https://notify-api.line.me/api/notify'

class Client(object):
    def __init__(self, token=None):
        self.token = token

    def set_token(self, token):
        self.token = token
        return self

    def _get_headers(self):
        if self.token is not None:
            return {'Authorization': f'Bearer {self.token}'}
        else:
            raise NoTokenError

    def send(self, content: str=None, file: str=None):
        if content is not None and 1 <= len(content) <= 1000:
            if file is not None:
                binary_image = open(file, mode='rb')
                try:
                    imageFile = {'imageFile': binary_image}
                    r = requests.post(LINE_API_URL, headers=self._get_headers(), data={'message': {content}}, files=imageFile)
                except Exception:
                    pass
                finally:
                    binary_image.close()
            else:
                r = requests.post(LINE_API_URL, headers=self._get_headers(), data={'message': {content}})