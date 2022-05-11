import requests
import json
import time


uri = "http://192.168.0.16:5000/chain"

res = json.loads(requests.get(uri).text)

#print(min(res['chain'][10]['transactions']))
with open('blocks.json', 'w') as file:
    json.dump(res, file)