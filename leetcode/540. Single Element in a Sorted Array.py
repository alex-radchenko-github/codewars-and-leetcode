def singleNonDuplicate(nums):
    #print(list(range(1, len(nums), 2)))
    for i in range(1, len(nums), 2):
        if nums[i] != nums[i-1]:
            return nums[i-1]
    return nums[-1]


print(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
print(singleNonDuplicate([1,1,2]))