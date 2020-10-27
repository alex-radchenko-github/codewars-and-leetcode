def isHappy(n):
    bn = []
    while n > 1:
        if n in bn:
            return False
        else:
            bn.append(n)
            a = map(lambda x: int(x)**2, list(str(n)))
            n = sum(list(a))
    return True


print(isHappy(2))
#print(isHappy(4))
