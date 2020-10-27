def twos_difference(lst):
    rez = []
    for i in lst:
        temp_rez = []
        if i < 2:
            continue
        else:
            if i-2 in lst:
                temp_rez.append(i-2)
                temp_rez.append(i)
        if len(temp_rez) != 0:
            rez.append(tuple(temp_rez))
            temp_rez = []
    return sorted(rez)

print(twos_difference([1, 2, 3, 4]))#, [(1, 3), (2, 4)])
print(twos_difference([1, 3, 4, 6]))#, [(1, 3), (4, 6)])
print(twos_difference([0, 3, 1, 4]))#, [(1, 3)])
print(twos_difference([4, 1, 2, 3]))#, [(1, 3), (2, 4)])
print(twos_difference([6, 3, 4, 1, 5]))#, [(1, 3), (3, 5), (4, 6)])
#print(twos_difference([3, 1, 6, 4]))#, [(1, 3), (4, 6)])
#print(twos_difference([1, 3, 5, 6, 8, 10, 15, 32, 12, 14, 56]))#, [(1, 3), (3, 5), (6, 8), (8, 10), (10, 12), (12, 14)])
#print(twos_difference([1, 4, 7, 10]))#, [])
#print(twos_difference([]))#, [])