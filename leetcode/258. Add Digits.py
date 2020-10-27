def addDigits(num):
    while len(list(str(num))) > 1:
        num = sum(int(i) for i in list(str(num)))
    return num

print(addDigits(38))