import bisect

def searchRange(nums,target):
    rez = []
    for i, n in enumerate(nums):
        if n == target:
            rez.append(i)
    if rez == []:
        return [-1,-1]
    elif len(rez) == 1:
        return [rez[0], rez[0]]
    elif len(rez) > 2:
        return [rez[0], rez[-1]]
    else:
        return rez

print(searchRange([5,7,7,8,8,10], 8))
#print(searchRange([5,7,7,8,8,10], 6))
#print(searchRange([], 0))
#print(searchRange([3,3,3], 3))