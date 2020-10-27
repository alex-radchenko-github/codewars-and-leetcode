def smallerNumbersThanCurrent(nums):
    rez = []
    for i in nums:
        rez.append(len(list(filter(lambda x: x < i, nums))))
    return rez

print(smallerNumbersThanCurrent([6, 5, 4, 8]))
