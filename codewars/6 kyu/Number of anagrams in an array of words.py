from itertools import combinations

def anagram_counter(words):
    return len([x for x in list(combinations(words, 2)) if sorted(x[0]) == sorted(x[1])])


#    rez = 0
#    for i in list(combinations(words, 2)):
#        if sorted(i[0])==sorted(i[1]):
#            rez +=1
#    return rez


print(anagram_counter(['dell', 'ledl', 'abc', 'cba']))  # , 2)
print(anagram_counter(['dell', 'ledl', 'lled', 'cba']))  # , 3)
print(anagram_counter(['dell', 'ledl', 'abc', 'cba', 'bca', 'bac', 'cab']))  # , 11)
