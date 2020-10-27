import collections
def findDuplicate(nums):
    rez = set()
    for n in nums:
        if n not in rez:
            rez.add(n)
        else:
            return n

print(findDuplicate([1,3,4,2,2]))
print(findDuplicate([2,2,2,2,2]))