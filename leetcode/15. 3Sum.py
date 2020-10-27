import itertools


def twoSum(target, nums):
    rez1 = []
    rez = {}
    print(nums)
    for i, num in enumerate(nums):
        n = -target - num
        if n not in rez:
            rez[num] = i
        else:
            rez1.append([rez[n], i, target])

    return rez1,


def threeSum(nums):
    rez = []
    nums = sorted(nums)
    print(nums)
    for i in range(1, len(nums)):
        n = nums[i - 1]
        l = nums[i:len(nums)]
        if n < 0:
            print(n, l)
        else:
            continue
        # twoSum(n, l)


# Метод перебора
#    rez = []
#    nums = itertools.combinations(nums,3)
#    for i in nums:
#        if sum(i) == 0 and sorted(i) not in rez:
#            rez.append(sorted(i))
#    return rez

#print(threeSum([-1, 0, 1, 2, -1, -4]))
print(twoSum(-1, [-1,0, 1, 2]))

# -4 [-1, -1, 0, 1, 2]
# -1 [-1, 0, 1, 2]
# 0 [1, 2]
# 1 [2]
# []
# print(threeSum([-10,-11,13,0,-11,9,1,-6,-1,-12,10,-9,0,-15,-13,4,-13,-1,-12,2,-11,-6,10,2,-6,6,-8,-12,11,-2,1,9,2,-1,-14,-1,-6,-6,0,0,-3,-4,-2,4,-12,-8,-7,-10,6,-11,-1,2,-2,-14,-10,7,7,-3,10,-4,3,-11,-10,12,3,13,-4,4,-8,4,-11,-4,-15,-6,-15,-12,1,-15,-15,14,-11,-8,2,-6,-7,-1,-14,-14,11,4,-3,-1,8,-6,-3,-12,-8,0,8,-1,11,4,2,11,14,2,6,-8,-6,-1,-8,-1,6]))
