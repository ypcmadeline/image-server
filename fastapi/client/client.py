import requests
import base64
import pymongo
from PIL import Image
from io import BytesIO
from loguru import logger



def client_post(name):
    folder = 'upload/'
    with open(folder+name,"rb") as f:
        contents = base64.b64encode(f.read()).decode()
    img = {'name': name, 'image': contents}
    r = requests.post(url, json=img)
    logger.info(r.status_code)

 
def client_get(name):
    r = requests.get(url, params={'name': name})
    path = 'download/dl_'
    img = r.json()['image']
    im = Image.open(BytesIO(base64.b64decode(img)))
    im.save(path+name, 'jpeg')
    logger.info(r.status_code)


if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/'
    img_name = 'IMG_4130.jpeg'
    # client_post(img_name)
    client_get(img_name)