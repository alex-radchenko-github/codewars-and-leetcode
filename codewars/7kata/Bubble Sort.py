def bubble(l):
    rez = []
    r = True
    while r:
        r = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                r = True
    return l


print(bubble([2,0,2,1,1,0]))
