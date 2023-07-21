import sys
import requests
import json

f = open(sys.argv[1])
url = 'https://ssd.jpl.nasa.gov/api/horizons_file.api'
r = requests.post(url, data={'format':'json'}, files={'input': f})
f.close()
data = r.json()
json.dump(data, open('result.json', 'w'))
