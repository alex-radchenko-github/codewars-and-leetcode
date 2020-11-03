def minStartValue(nums):

    rez = 0
    rez_t = []
    for i in nums:
        rez += i
        rez_t.append(rez)
    return 1 if min(rez_t) > 0 else abs(min(rez_t)) + 1

print(minStartValue([-3,2,-3,4,2]))
print(minStartValue([1,-2,-3]))