input_str = input("Input a string: ")
d = dict()
for word in input_str.split():
    if word not in d:
        d[word] = 1
        #print(d)
    else:
        d[word] += 1
        #print(d)
print(d)