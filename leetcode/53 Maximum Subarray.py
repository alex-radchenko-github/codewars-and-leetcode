def max_sequence(nums):
    m = float('-inf')
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        if s > m:
            print(s, m)
            m = s
        if s < 0:
            print(s, m)
            s = 0
    #return m
print(max_sequence([-2,1,-3,4,-1,2,1,-5,4]))
#[4,-1,2,1], 6
