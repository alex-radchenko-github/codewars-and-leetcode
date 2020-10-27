def pivotIndex(nums):
    rez = []
    S = sum(nums)
    ls = 0
    for i, n in enumerate(nums):
        if ls == S - ls-n:
            rez.append(i)
        ls += n
    return min(rez)


#print(pivotIndex([1, 7, 3, 6, 5, 6]))
# print(pivotIndex([-1,1,-1,1,-1,0]))
print(pivotIndex([-1,1,-1,1,-1,0]))
