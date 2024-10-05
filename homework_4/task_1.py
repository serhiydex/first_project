list = input("Insert string: ")

if len(list) < 2:
    print("Empty String")
else:
    print(list[0:2] + list[-2:])

