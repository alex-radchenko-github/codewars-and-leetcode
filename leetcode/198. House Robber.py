def rob(nums):
    nums = [0] + nums + [0]
    print(nums, list(range(3, len(nums))))
    for i in range(3, len(nums)):
        nums[i] = nums[i] + max(nums[i - 2], nums[i - 3])

    return max(nums)


print(rob([2,1,1,2]))