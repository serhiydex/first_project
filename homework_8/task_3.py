
def make_operation(a, *args):

    if a == '+':
        s = 0
        for i in args:
            s += i
    elif a == '-':
        s = 0
        for i in args:
            s = s - i
    elif a == '*':
        s = 1
        for i in args:
            s = s * i

    return s


