def heightChecker(heights):
    return len(list(filter(lambda x: x[0]!=x[1], list(zip(heights, sorted(heights))))))

#    return list(zip(heights, sorted(heights)))
print(heightChecker([1,1,4,2,1,3]))
print(heightChecker([5,1,2,3,4]))