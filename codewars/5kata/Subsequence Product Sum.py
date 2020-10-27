import itertools


def moltipl(lst):
    var = 1
    for i in lst:
        var *= i
    return var


def product_sum(a, m):
    lst2 = list(itertools.combinations(a, m))
    for i in lst2:
        print(moltipl(i), sum(i))

    return sum(list(map(moltipl, lst2))), lst2


# print(product_sum([2, 3, 4, 5], 3))#, 154),
# print(product_sum([1, 2, 3], 2))#, 11),
#print(product_sum([5, 7, 2, 3], 3))  # , 247),
print(product_sum([3, 10, 7, 9, 1, 4, 5, 2, 8, 6], 7))#, 8409500),
# print(product_sum([10, 7, 8, 5, 6, 9, 4, 1, 2, 3], 8))#, 12753576),
# print(product_sum([1, 7, 6, 10, 21, 5, 9, 8, 5, 4], 2))#, 2469)
# print(product_sum([6, 7, 8, 5, 2, 4, 9, 3, 1, 10], 6))#, 3416930),
# print(product_sum([3, 2, 9, 1, 7, 10, 5, 6, 8, 4], 4))#, 157773),
# print(product_sum([9, 8, 10, 4, 2, 7, 5, 1, 3, 6], 3))#, 18150),
# print(product_sum([3, 3, 1, 7, 6, 8, 1, 4, 6, 10], 4))#, 94837),
# print(product_sum([6, 8, 1, 7, 2, 10, 5, 9, 3, 4], 5))#, 902055),
# print(product_sum([10, 3, 4, 9, 5, 8, 6, 7, 1, 2], 1))#, 55),
# print(product_sum([7, 9, 4, 2, 3, 10, 8, 6, 5, 1], 9))#, 10628640)

# 2345
