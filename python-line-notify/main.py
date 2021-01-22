import requests

import env

LINE_API_URL = 'https://notify-api.line.me/api/notify'

class NoTokenError(Exception):
    pass

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
            raise NoTokenError(f'Line notify token is not set.')

    def send_massage(self, content: str):
        if len(content) <= 1000:
            r = requests.post(LINE_API_URL, headers=self._get_headers(), data={'message': {content}})

    def send_massage_and_image(self, content: str, image_path: str):
        binary_image = open(image_path, mode='rb')
        image = {'imageFile': binary_image}
        r = requests.post(LINE_API_URL, headers=self._get_headers(), data={'message': {content}}, files=image)

def main():
    client = Client(env.TOKEN)
    client.send_massage('test')

if __name__ == '__main__':
    main()