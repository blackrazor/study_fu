import requests
import json
import random
import numpy as np
import time
trans_uri = "http://192.168.0.16:5000/transactions/new"
mine_uri = "http://192.168.0.16:5000/mine"



sender_list = [x for x in range(5000)]
amount_list = np.random.normal(4000,1000, 10000) 
num_requests = 1000

last_mine = 0


ts_trans_diffs = [x for x in range(30,300)]
for i in range(1,16):
    ts_trans_diffs.extend([i] * i)
to_mine = random.choice(ts_trans_diffs)

sender_list_ddos = [x for x in range(5000, 5100)]
amount_list_ddos = [x for x in range(100, 130)]
ts_trans_diffs_ddos = [x for x in range(1,4)]

last_ddos = 0
ts_ddos_diffs = [x for x in range(0,1)]

timeframe = time.time()
block_timeframe = timeframe

last_ddos_ts = block_timeframe
block_id = 1

ddos_block_ids = [x for x in range(1,1000)]
ddos_block_ids = random.sample(ddos_block_ids, 100)

last_ddos = 0
cnt = 0
delays = [0.1,0.2,0.3,0.5,0.6,0.7,0.8,0.9,1]

print(ddos_block_ids)

def send_ddos(timeframe):
    sender = str(random.choice(sender_list_ddos))
    recipient = str(random.choice(sender_list_ddos))
    amount = random.choice(amount_list_ddos)
    timeframe += 0.02
    if sender == recipient:
        recipient+=str(random.choice(sender_list))

    msg = json.dumps({
        'sender' : sender, 'recipient': recipient, 'amount': abs(amount), "time": timeframe
    })

    requests.post(url=trans_uri,json=msg)
    return timeframe

for id in range(100000):
    if cnt == 200:
        requests.get(url=mine_uri)
        to_mine = random.choice(ts_trans_diffs)
        last_mine = id
        block_timeframe = max(last_ddos_ts,timeframe)
        block_id += 1
        last_ddos_ts = block_timeframe
        cnt = 0
    if id - last_ddos > random.choice(ts_trans_diffs_ddos) and  block_id in ddos_block_ids:
        last_ddos = id
        for _ in range(300):
            last_ddos_ts += 1
            send_ddos(last_ddos_ts)

    sender = str(random.choice(sender_list))
    recipient = str(random.choice(sender_list))
    amount = random.choice(amount_list)
    timeframe += random.choice(delays)
    if sender == recipient:
        recipient+=str(random.choice(sender_list))

    msg = json.dumps({
        'sender' : sender, 'recipient': recipient, 'amount': abs(amount), "time": timeframe
    })

    requests.post(url=trans_uri,json=msg)

    cnt+=1

ddos_block_ids = [x for x in ddos_block_ids if x <= block_id]

with open('ddosed_blocks.json', 'w') as file:
   json.dump(ddos_block_ids, file)