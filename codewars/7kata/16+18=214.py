def add(num1, num2):
    if len(list(str(num1))) == len(list(str(num2))):
        num1 = list(str(num1))
        num2 = list(str(num2))
    elif len(list(str(num1))) > len(list(str(num2))):
        num1 = list(str(num1))
        num2 = list(str(num2))
        num2.insert(0, "0")
    else:
        num1 = list(str(num1))
        num2 = list(str(num2))
        num1.insert(0, "0")
    rez = []
    for i in range(len(num1)):
        rez.append(str(int(num1[i]) + int(num2[i])))
    return int(''.join(rez))


print(add(16,18))#, 214)
print(add(26, 39))  # , 515)
print(add(81,122))#, 1103)
print(add(29151,311629))#, 33107710)

