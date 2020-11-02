import itertools

def maximumProduct(nums):
    print(sorted(nums))
    return max(sorted(nums)[-1]*sorted(nums)[-2]*sorted(nums)[-3], sorted(nums)[0]*sorted(nums)[1]*sorted(nums)[-1])

print(maximumProduct([1,2,3,4]))
print(maximumProduct([-1,-2,-3]))
print(maximumProduct([-100,-98,-1,2,3,4]))