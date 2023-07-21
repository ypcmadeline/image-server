import PIL.Image as Image
from io import BytesIO

with open("test.jpeg","rb") as f:
    contents = f.read()
img = Image.open(BytesIO(contents))
img.save('recieved.jpeg')

# import requests

# url = 'http://127.0.0.1:8000'
# files = {'image': open('img/test.jpeg', 'rb')}
# requests.post(url, files=files)