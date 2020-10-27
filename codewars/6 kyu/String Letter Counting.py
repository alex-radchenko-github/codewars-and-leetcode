import collections
def letter_count(s):
    return collections.Counter(s)




"""
Мой вариант
    rez = {}
    s1 = sorted(set(s))
    for i in s1:
        rez[i] = s.count(i)
    return rez
"""


#print(letter_count("codewars"))#, {"a": 1, "c": 1, "d": 1, "e": 1, "o": 1, "r": 1, "s": 1, "w": 1})
print(letter_count("activity"))#, {"a": 1, "c": 1, "i": 2, "t": 2, "v": 1, "y": 1})
#print(letter_count("arithmetics"))#, {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2})
#print(letter_count("traveller"))#, {"a": 1, "e": 2, "l": 2, "r": 2, "t": 1, "v": 1})
#print(letter_count("daydreamer"))#, {"a": 2, "d": 2, "e": 2, "m": 1, "r": 2, "y": 1})