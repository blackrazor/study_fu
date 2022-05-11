import requests
import json
import random
import numpy as np
import time
trans_uri = "http://192.168.0.16:5000/transactions/new"
mine_uri = "http://192.168.0.16:5000/mine"



sender_list = [x for x in range(1000)]
amount_list = np.random.normal(5000,1000, 10000) 
num_requests = 1000

last_mine = 0

ts_list_diffs = [x for x in range(10)]

mine_iterate_list = [x for x in range(30,300)]
for i in range(1,16):
    mine_iterate_list.extend([i] * (16 - i))
mine_iterate_list.extend([0]* 3)
to_mine = random.choice(mine_iterate_list)


timeframe = time.time()

for id in range(100000):
    if id - last_mine > to_mine:
        requests.get(url=mine_uri)
        to_mine = random.choice(mine_iterate_list)
        last_mine = id

    sender = str(random.choice(sender_list))
    recipient = str(random.choice(sender_list))
    amount = random.choice(amount_list)
    timeframe += random.choice(mine_iterate_list)
    if sender == recipient:
        recipient+=str(random.choice(sender_list))

    msg = json.dumps({
        'sender' : sender, 'recipient': recipient, 'amount': amount, "time": timeframe
    })

    requests.post(url=trans_uri,json=msg)