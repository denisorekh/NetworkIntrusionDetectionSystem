from modules.mlp import Mlp

import random

with open("data/weights.txt", "r+") as r:
    t = r.read().split()
    if not len(t):
        t = []
        for i in range(7233):
            t.append(random.uniform(-1, 1))
        r.write("\n".join(map(str, t)))
        test_mlp = Mlp(t)
