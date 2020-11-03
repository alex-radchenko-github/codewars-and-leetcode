import collections
def frequencySort(s):
    rez = ""
    x1 = dict(collections.Counter(s))
    list_d = list(x1.items())
    list_d.sort(key=lambda i: i[1])
    for i in list_d[::-1]:
        x2 = i[0]*i[1]
        rez += x2
    return rez

print(frequencySort("tree"))#eert
print(frequencySort("cccaaa"))#cccaaa