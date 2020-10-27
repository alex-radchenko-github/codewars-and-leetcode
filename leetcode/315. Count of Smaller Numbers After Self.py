from bisect import insort, bisect_left

def countSmaller(nums):
    rez = {}
    rez2 = {}
    rez3 = []
    for i,n in enumerate(nums):
        rez[n] = i
    for i in sorted(nums):
        rez2[i] = rez[i]
    for i in rez2:
        rez3.append(bisect_left(rez2), i)
    return rez, nums, rez2, rez3
print(countSmaller([5,2,6,1]))