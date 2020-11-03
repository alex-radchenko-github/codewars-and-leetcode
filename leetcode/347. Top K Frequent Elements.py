import collections
def topKFrequent(nums, k):
    print(collections.Counter(nums).most_common(k))
    return [i[0] for i in sorted(list(collections.Counter(nums).items()), key=lambda i: i[1], reverse=True)[:k]]
print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([3,2,2,1,1,1], 2))