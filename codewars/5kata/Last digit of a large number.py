def last_digit(n1, n2):
    stepen = int(str(int(str(n2)[-2:]) % 4)[-1])
    if stepen == 0:
        stepen = 4
    return int(str(int(str(n1)[-1]) ** stepen)[-1])

print(last_digit(4, 1))#, 4)
print(last_digit(4, 2))#, 6)
print(last_digit(9, 7))#, 9)
print(last_digit(10, 10 ** 10))#, 0)
print(last_digit(2 ** 200, 2 ** 300))#, 6)
print(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651))#, 7)
