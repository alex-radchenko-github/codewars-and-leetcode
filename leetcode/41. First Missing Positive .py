import random
import time
import string


def firstMissingPositive(nums):
    n = 0
    range
    for i in sorted(set(nums)):
        if i <= 0:
            continue
        elif n + 1 == i:
            n = n+1
            continue
        elif n + 1 != i:
            break
    return n+1
print(firstMissingPositive([0,2,2,1,1]))