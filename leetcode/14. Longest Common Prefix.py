def longestCommonPrefix(strs):
    rez = []
    print(list(zip(*strs)))
    for i in zip(*strs):
        if len(set(i)) == 1:
            rez.append(list(set(i))[0])
        elif len(set(i)) != 1:
            break
    return ''.join(rez)

#    if strs == []:
#        return ""
#    for i in range(min(map(lambda x: len(x),strs))):
#        if len(set(list(map(lambda x: x[:min(map(lambda x: len(x),strs))-i],strs)))) == 1:
#            return list(set(list(map(lambda x: x[:min(map(lambda x: len(x),strs))-i],strs))))[0]
#    return ""

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["cir","car"]))
