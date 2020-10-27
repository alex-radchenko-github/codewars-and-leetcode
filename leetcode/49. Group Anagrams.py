import string
import itertools
import collections
def groupAnagrams(strs):
    d = collections.defaultdict(list)
    for i in strs:
        d["".join(sorted(i))].append(i)
    return d.values()
#    rez = []
#    d_rez = {}
#    tmp1 = []
#    for i in strs:
#        tmp1.append("".join(sorted(i)))
#    tmp1 = sorted(set(tmp1))
#    d_rez = d_rez.fromkeys(tmp1, "")
#    for i in strs:
#        d_rez["".join(sorted(i))] = d_rez.get("".join(sorted(i))) + i + ","
#    for i in list(d_rez.values()):
#        rez.append(i.split(",")[:-1])
#    return rez


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
#print(groupAnagrams(["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]))
#print(groupAnagrams(["ddddddddddg","dgggggggggg"]))#[["dgggggggggg"],["ddddddddddg"]]
