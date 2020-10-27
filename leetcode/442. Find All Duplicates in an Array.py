import collections
def findDuplicates(nums):
    nums = dict(collections.Counter(nums))
    for i in nums:
        print(nums.get(i))
    print(sorted(list(filter(lambda x: nums.get(x) == 2, dict(collections.Counter(nums))))))
print(findDuplicates([4,3,2,7,8,2,3,1]))