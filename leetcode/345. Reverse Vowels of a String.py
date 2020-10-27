def reverseVowels(s):
    t1 = []
    t2 = []
    vc = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    for i in s:
        if i not in vc:
            t1.append(i)
        else:
            t1.append("")
            t2.append(i)
    t2 = t2[::-1]
    for i, n in enumerate(t1):
        if t1[i] == '':
            t1[i] = t2[0]
            t2.pop(0)
    return "".join(t1)

#    for i in range(len(t1)):
#        if t1[i] == '':
#            t1[i] = t2[0]
#            t2.pop(0)
#    return "".join(t1)

#print(reverseVowels("aA"))
print(reverseVowels("leetcode"))#"leotcede"