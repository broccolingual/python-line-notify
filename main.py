import requests

import env

LINE_API_URL = 'https://notify-api.line.me/api/notify'
TOKEN = env.TOKEN

def _get_headers(token):
    return {'Authorization': f'Bearer {token}'}

def send_massage(content: str):
    r = requests.post(LINE_API_URL, headers=_get_headers(TOKEN), data={'message': {content}})
    return r.status_code

def send_massage_and_image(content: str, image_path: str):
    binary_image = open(image_path, mode='rb')
    image = {'imageFile': binary_image}
    r = requests.post(LINE_API_URL, headers=_get_headers(TOKEN), data={'message': {content}}, files=image)
    return r.status_code

def main():
    send_massage('This is test!')
    send_massage_and_image('image', './test/test.png')

if __name__ == '__main__':
    main()