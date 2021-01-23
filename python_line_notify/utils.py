import re
from io import BytesIO
from urllib.request import urlopen
from urllib.parse import urlparse

from PIL import Image

def is_url(string) -> bool:
    o = urlparse(string)
    if o.scheme in ['http', 'https']:
        return True
    else:
        return False

def is_jpg(url) -> bool:
    pattern = r'.+\.jpg'
    result = re.match(pattern, url)
    if result:
        return True
    else:
        return False

def get_image_size(url) -> tuple:
    f = BytesIO(urlopen(url).read())
    img = Image.open(f)
    return (img.width, img.height)