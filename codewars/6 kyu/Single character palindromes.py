def solve(s):
    s = list(s)
    if s == s[::-1]:
        return "OK"

    for i in range(len(s)):
        t = s[i]
        s.pop(i)
        if s == s[::-1]:
            return "remove one"
        else:
            s.insert(i, t)
    return "not possible"


print(solve("abba"))  # ,"OK")
print(solve("abbaa"))  # ,"remove one")
print(solve("abbaab"))  # ,"not possible")
print(solve("madmam"))  # ,"remove one")
print(solve("raydarm"))  # ,"not possible")
print(solve("hannah"))  # ,"OK")
