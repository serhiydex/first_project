phone_number = input("Enter phone number:")
if len(phone_number) == 10 and phone_number.isdigit():
    print("You have entered the correct number format ")
else:
    print("Enter the phone number again")