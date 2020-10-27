def find_subarr_maxsum(arr):
    rez = []
    if arr == []:
        return 0
    max_n = float('-inf')
    min_n = 0
    for i in range(len(arr)):
        min_n += arr[i]
        if min_n >= max_n:
            max_n = min_n
            rez.append(arr[i])
        if min_n < 0:
            min_n = 0
    return rez
print(find_subarr_maxsum([4, -1, 2, 1, -40, 1, 2, -1, 4]))# [[[4, -1, 2, 1], [1, 2, -1, 4]], 6]) [0-3] [5-8]
print(find_subarr_maxsum([-4, -1, -2, -1, -40, -1, -2, -1, -4]))#
print(find_subarr_maxsum([2, 1, 3, 4, 1, 2, 1, 5, 4]))#