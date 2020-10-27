import collections
def singleNumber(nums):
    x = dict(collections.Counter(nums))
    for i in x:
        if x[i] == 1:
            return i

print(singleNumber([4,1,2,1,2]))