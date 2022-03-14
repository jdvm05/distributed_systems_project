import random
import time

import numpy as np
import redis

print("RUN THIS INSTEAD!!")
iteration = 1
r = redis.from_url('redis://redis:6379')

while True:
    if iteration == 1:
        data = {"sensor":"L2_Temperature",
            "value": np.random.random()}
        iteration = 2
    elif iteration == 2:
        data = {"sensor":"L2_Pressure",
            "value": np.random.random()}
        iteration = 3
    elif iteration == 3:
        data = {"sensor":"L2_Level",
            "value": np.random.random()}
        iteration = 1
    print("send:", r.xadd("IOT", data), data)

    time.sleep(1)
