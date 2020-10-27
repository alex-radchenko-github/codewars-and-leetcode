from itertools import groupby
from collections import Counter

def longest_repetition(chars):
    return list(map(lambda x: list(x[1]), groupby(chars)))


#    rez = []
#    for i in groupby(chars):
#        rez.append([i[0], len(list(i[1]))])
#    #for i in groupby(chars):
#    #    print(list(i[1]))
#    return tuple(max(rez, key=lambda x: x[1], default=('', 0)))

#    rez = [0,""]
#    t1 = [1, chars[0]]
#    for i in range(len(chars)-1):
#        if chars[i] == chars[i+1]:
#            t1[0] = t1[0] + 1
#            t1[1] = chars[i]
#            if i == range(len(chars)-1)[-1]:
#                if t1[0] > rez[0]:
#                    rez = t1
#        elif chars[i] != chars[i+1]:
#            if t1[0] > rez[0]:
#                rez = t1
#            t1 = [1, ""]
#    rez.reverse()
#    return tuple(rez)

print(longest_repetition("bbbaaabaaaa"))#('a', 4)