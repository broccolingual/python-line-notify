import requests

from .exceptions import *
from python_line_notify.utils import get_image_size, is_jpg, is_url

LINE_API_URL = 'https://notify-api.line.me/api/notify'

class Client(object):
    def __init__(self, token=None):
        self.token = token

    def set_token(self, token: str):
        """Line Notifyのトークンを設定

        Parameters
        ----------
        token: str
            Line Notifyから発行されたトークン
        """
        self.token = token
        return self

    def _get_headers(self):
        if self.token is not None:
            return {'Authorization': f'Bearer {self.token}'}
        else:
            raise NoTokenError

    def send(self, content: str=None, image: str=None, sticker: tuple=None, notify: bool=True):
        """Line Notifyにメッセージを送る

        Parameters
        ----------
        content: str, default None
            本文の内容(省略不可)

        image: str, default None (optional)
            画像の相対パス もしくは 画像URL(jpgのみ)

        sticker: tuple, default None (optional)
            第1引数: StickerPackageID: int
            第2引数: StickerID: int
            ※どちらも必須

        notify: bool, default True (optional)
            True: 通知される(デフォルト)
            False: 通知されない
        """
        if content is not None and 1 <= len(content) <= 1000:
            payload = {"message": content}
            imageFile = None

            if image is not None:
                if is_url(image) is True and is_jpg(image) is True:
                    width, height = get_image_size(image)
                    if width <= 2048 and height <= 2048: 
                        payload.update({
                            'imageThumbnail': image,
                            'imageFullsize': image,
                        })

                elif is_url(image) is False:
                    binary_image = open(image, mode='rb')
                    imageFile = {'imageFile': binary_image}

            if notify is False:
                payload.update({
                    'notificationDisabled': 'true',
                })

            if sticker is not None:
                payload.update({
                    'stickerPackageId': sticker[0],
                    'stickerId': sticker[1],
                })
            
            r = requests.post(LINE_API_URL, headers=self._get_headers(), data=payload, files=imageFile)
            return r