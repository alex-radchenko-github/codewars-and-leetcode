import collections
def minSteps(s,t):
    rez = []
    t = collections.Counter(t)
    s = collections.Counter(s)
    for i in s:
        if (s[i]-t[i]) >0:
            rez.append((s[i]-t[i]))
    return sum(rez)

print(minSteps("leetcode", "practice"))
