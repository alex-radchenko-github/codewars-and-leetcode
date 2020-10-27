def lu(s):
    if s.islower():
        return s.upper()
    else:
        return s.lower()

def work_on_strings(a, b):
    a_t = a.lower()
    b_t = b.lower()
    rez = ""
    rez2 = ""
    for i in a:
        if b_t.count(i.lower()) % 2 == 0:
            rez += i
        else:
            rez += lu(i)
    for i in b:
        if a_t.count(i.lower()) % 2 == 0:
            rez2 += i
        else:
            rez2 += lu(i)
    return rez+rez2


#print(work_on_strings("abc", "cde"))  # , "abCCde")
# print(work_on_strings("abcdeFgtrzw", "defgGgfhjkwqe"))#, "abcDeFGtrzWDEFGgGFhjkWqE")
print(work_on_strings("abcdeFg", "defgG"))#, "abcDEfgDEFGg")
# print(work_on_strings("abab", "bababa"))#, "ABABbababa")
