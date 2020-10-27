def missingNumber(nums):
    return (len(nums)*(len(nums)+1)//2) - sum(nums)

#    try:
#        return list((set(range(max(nums)+1)).difference(set(sorted(nums)))))[0]
#    except IndexError:
#        return max(nums)+1

print(missingNumber([9,6,4,2,3,5,7,0,1]))
print(missingNumber([0,1]))