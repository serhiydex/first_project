import random

list = random.sample(range(1, 101), 100)
print(list)
res = []
for i in list:
    if i % 7 == 0 and i % 5 != 0:
        res.append(i)
print(res)
