import random

ch_1 = random.randrange(1, 10)
ch_2 = int(input("Enter a number between 1 and 10: "))
print(ch_1)
while ch_2 != ch_1:
    print("Enter a number again")


print("You guessed the number")


