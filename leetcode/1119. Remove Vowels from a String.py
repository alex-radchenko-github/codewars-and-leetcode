def removeVowels(S):
    return "".join(filter(lambda x: x not in ['a', 'e', 'i', 'o', 'u'], S))
print(removeVowels("leetcodeisacommunityforcoders"))