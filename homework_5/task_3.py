import random

string = input("Input the word: ")
counter = 0
while counter <= 4:
    x = random.sample(string, k = len(string))
    print(x)
    counter += 1