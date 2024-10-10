import random

list_1 = random.sample(range(1, 11), 10)
list_2 = random.sample(range(1, 11), 10)
res = []
for num in list_1:
    if num not in res:
        res.append(num)
for num in list_2:
    if num not in res:
        res.append(num)
print(res)