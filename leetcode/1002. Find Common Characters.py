import collections


def commonChars(A):
    rez = []
    t1 = ""
    for i in A:
        t1 += i
    for i in A:
        for i1 in i:
            rez.append(i.count(i1))
    return rez
#print(commonChars(["bella", "label", "roller"]))
print(commonChars(["cool","lock","cook"]))
