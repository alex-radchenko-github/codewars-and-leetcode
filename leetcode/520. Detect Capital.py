def detectCapitalUse(word):
    if list(set(list(map(lambda x: x.isupper(), list(word))))) == [True] or list(
            set(list(map(lambda x: x.isupper(), list(word))))) == [False]:
        return True
    elif list(map(lambda x: x.isupper(), list(word)))[0] == True and list(set(list(map(lambda x: x.islower(), list(word)))[1:]))[0] == True:
        return True
    else:
        return False

    #return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())


print(detectCapitalUse("USA"))
print(detectCapitalUse("leetcode"))
print(detectCapitalUse("Google"))
print(detectCapitalUse("Leetcode"))
print(detectCapitalUse("FlaG"))
