def twoSum(nums, target):
    rez = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in rez:
            rez[num] = i
            print(rez)
        else:
            return [rez[n], i]
    return set(nums).difference(range(1, max(nums)+1))

#print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
#print(twoSum([3,3,5], 6))

#7 = 9-2
