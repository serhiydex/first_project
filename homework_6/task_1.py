import random

r_list = random.sample(range(0, 100), 10)
big_num = 0
for i in r_list:
    while i > big_num:
        big_num += 1
print(big_num)




