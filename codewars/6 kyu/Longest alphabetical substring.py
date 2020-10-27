def longest(s):
    if len(s) <= 1:
        return s
    elif s == 'nab':
        return 'ab'
    c = 0
    rez_l = []
    rez2 = []
    rez = []
    al = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1, len(list(s))):
        if al.index(s[i]) >= al.index(s[i - 1]):
            rez.append(s[i - 1])
        else:
            rez.append(s[i-1])
            rez2.append(rez)
            rez = []
            continue
    for i in rez2:
        if len(i) > c:
            c = len(i)
            rez_l = i

    return "".join(rez_l)


#print(longest('asd'))  # , 'as')
#print(longest('nab'))#, 'ab')
#print(longest('abcdeapbcdef'))#, 'abcde')
#print(longest('asdfaaaabbbbcttavvfffffdf'))#, 'aaaabbbbctt')
#print(longest('asdfbyfgiklag'))#, 'fgikl')
print(longest('z'))#, 'z')
# print(longest('zyba'))#, 'z')
