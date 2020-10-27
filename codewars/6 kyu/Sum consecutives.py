def sum_consecutives(s):
    rez = []
    cop = float('-inf')
    count_n = 0
    for i in s:
        if i != cop:
            count_n = 0
            rez.append(i)
            count_n = 0
            cop = i
        if i == cop:
            count_n += 1
            rez[-1] = i * count_n
    return rez

print(sum_consecutives([0, 1, 1, 2, 2]))