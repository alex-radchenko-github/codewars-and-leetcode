import collections
def subarraySum(A, K):
    P = [0]
    for x in A:
        P.append((P[-1] + x) % K)
        print(P)

    count = collections.Counter(P)
    print(count)
    return list(v * (v - 1) / 2 for v in count.values())


print(subarraySum([4,5,0,-2,-3,1], 5))