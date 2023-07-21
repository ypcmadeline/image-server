from fastapi import FastAPI, Request
import uvicorn
from mongo import get_database
import pymongo
from loguru import logger
import base64


app = FastAPI()

db = get_database() 
image_coll = db['image_collection']

@app.post('/')
async def upload(recieved: Request):
    recieved = await recieved.json()
    image = recieved['image']
    image = base64.b64decode(image)
    name = recieved['name']
    sof0 = image.find(b'\xff\xc0')
    h = int.from_bytes(image[sof0+5:sof0+7], byteorder='big')
    w = int.from_bytes(image[sof0+7:sof0+9], byteorder='big')
    record = {'_id': name, 'height': h, 'width': w, 'image': image}
    try:
        image_coll.insert_one(record)
    except pymongo.errors.DuplicateKeyError:
        return {'Duplicate image'}
    return {'_id': name, 'height': h, 'width': w,} 
    

@app.get('/')
async def download(name: str):
    res = image_coll.find({'_id': name}, {'image': 1})[0]
    # logger.debug(type(res))
    if not res:
        return {'Not Found'}
    image = res['image']
    logger.debug(type(image))
    image = base64.b64encode(image).decode()
    return {'image': image}
   

uvicorn.run(app, host="0.0.0.0")


