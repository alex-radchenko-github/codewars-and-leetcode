def longestPalindrome(s):
    for i in range(1,len(s)+1)[::-1]:
        for i1 in range(len(s)+1-i):
            if s[i1:i1+i] == s[i1:i1+i][::-1]:
                return s[i1:i1+i]
print(longestPalindrome("babad"))
