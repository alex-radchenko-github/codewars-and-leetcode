def move_zeroes(nums):
    reg_01 = True
    while reg_01:
        reg_01 = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                reg_01 = True
    cou = nums.count(0)
    for i in range(cou):
        nums.remove(0)
        nums.append(0)
    return nums


print(move_zeroes([0, 3, 0, 1, 9, 6]))
