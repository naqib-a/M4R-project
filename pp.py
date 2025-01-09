import numpy as np

tries = []
rands = []
for i in range(100000):
    x = [1,2]
    while min(x)>0:
        new = np.random.randint(0,3)
        if new == 0:
            x[0] -= 1
            x[1] += 1
        else:
            x[0] += 1
            x[1] -= 1
    tries.append(np.argmax(x))
print(tries)
print(1-np.mean(tries))
