import itertools
def numIdenticalPairs(nums):
    n = 0
    for i in list(itertools.combinations(filter(lambda x: nums.count(x) >1, nums),2 )):
        if i[0]==i[1]:
            n +=1
    return n
print(numIdenticalPairs([1,1,1,1]))
print(numIdenticalPairs([1,2,3,1,1,3]))
print(numIdenticalPairs([1,2,3]))