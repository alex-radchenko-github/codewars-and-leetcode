def removeDuplicates(nums):
    rez = []
    for x in nums:
        if x in rez:
            continue
        else:
            rez.append(x)
    return rez
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))