def isPalindrome(s):
    rez = s.lower()
    rez2 = []
    for x in rez:
        if x.isalnum() == True:
            rez2.append(x)
    return "".join(rez2) == "".join(rez2)[::-1]
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("0P"))