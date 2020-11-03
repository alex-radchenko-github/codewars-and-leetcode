import collections
def firstUniqChar(s):
    if s == "":
        return -1
    elif len(s) == 1:
        return 0
    elif len(set(s)) == 1:
        return -1
    x1 = dict(collections.Counter(s))
    for i in range(len(s)):
        if x1[s[i]] == 1:
            return i
    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aadadaad"))