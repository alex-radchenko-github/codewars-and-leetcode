def backspaceCompare(S, T):
    rez_l = []
    rez = ""
    S = S[::-1]
    coun1 = 0
    for i in S:
        if i != "#" and coun1 == 0:
            rez += i
        elif i != "#" and coun1 > 0:
            coun1 -= 1
            continue
        elif i == "#":
            coun1 += 1
    rez_l.append(rez[::-1])

    rez = ""
    T = T[::-1]
    coun1 = 0
    for i in T:
        if i != "#" and coun1 == 0:
            rez += i
        elif i != "#" and coun1 > 0:
            coun1 -= 1
            continue
        elif i == "#":
            coun1 += 1
    rez_l.append(rez[::-1])
    print(rez_l, S, T)
    return rez_l[0] == rez_l[1]


print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("a###c", "#a#c"))
print(backspaceCompare("a#c", "b"))
print(backspaceCompare("ab##", "c#d#"))
