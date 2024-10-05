first_number = int(input("Enter the first number"))
second_number = int(input("Enter the second number"))
print(f"How much, {first_number} + {second_number}?")
result = int(input("Enter result"))
if first_number + second_number == result:
    print("Your answer is correct")
else:
    print("Try again")
