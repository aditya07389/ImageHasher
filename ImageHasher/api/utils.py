import hashlib
import requests
from PIL import Image
import imagehash
from io import BytesIO

def calculate_md5(image_content):
    return hashlib.md5(image_content).hexdigest()

def calculate_phash(image_content):
    image = Image.open(BytesIO(image_content))
    return str(imagehash.phash(image))
