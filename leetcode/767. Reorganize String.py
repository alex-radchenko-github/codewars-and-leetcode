import collections
import heapq


def reorganizeString(S):
    rez_f_l = ''
    rez = []
    x = collections.Counter(list(S))
    max_l = (len(S) + 1) / 2
    print(x, max_l)
    for i in x.values():
        if i > max_l:
            return ""
    for i1 in x:
        rez.append([x[i1], i1])
    c = sum(list(x.values()))
    temp_list = sorted(rez)[::-1]
    for i in temp_list:
        rez_f_l += i[0] * i[1]
    data = [""] * temp_list[0][0]
    rez_f_l = list(rez_f_l)
    #print(temp_list[0][0])
    while len(rez_f_l) != 0:
        co = 0
        while co < temp_list[0][0]:
            try:
                data[co] += rez_f_l[0]
            except IndexError:
                break
            rez_f_l.pop(0)
            co += 1
        else:
            co = 0
    return "".join(data)

#    x1 = heapq.heappop(temp_list)
#    rez_f = list()
#    for i1 in range(x1[0]):
#        rez_f.append([])
#    for i2 in range(x1[0]):
#        rez_f[i2].append(x1[1])
#
#
#    x1 = heapq.heappop(temp_list)
#    for i3 in range(x1[0]):
#        rez_f[i3].append(x1[1])
#    x1 = heapq.heappop(temp_list)
#
#
#    for i3 in range(len(rez_f)):
#        if len(rez_f[i3])>1:
#            continue
#        else:
#            rez_f[i3].append(x1[1])
#    for i in rez_f:
#        rez_f_l += "".join(i)
#
#    return rez_f, rez_f_l#, x1, temp_list#rez_f, c, rez[0][0], sorted(rez)[::-1], x1
#
#
#print(reorganizeString("aab"))
print(reorganizeString("vvvloo"))  # "vlvov"
