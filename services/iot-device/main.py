import random
import time

import numpy as np
import redis

print("RUN THIS INSTEAD!!")

r = redis.from_url('redis://redis:6379')

while True:

    data = {"sensor": random.choice(["L1_Temperature","L1_Pressure","L1_Level"]),
            "value": np.random.random()}

    print("send:", r.xadd("IOT", data), data)

    time.sleep(1)
