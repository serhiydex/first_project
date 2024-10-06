import random

ch_1 = int(input("Enter a number between 1 and 10: "))
ch_2 = random.randrange(1, 10)
print(ch_2)
while ch_1 != ch_2:
    ch_1 = int(input("Enter a number again: "))
print("You guessed the number")


