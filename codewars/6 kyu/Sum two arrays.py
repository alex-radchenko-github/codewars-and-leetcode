def sum_arrays(array1,array2):
    rez = []
    n1 = ""
    n2 = ""
    if array1 == [] and array2 == []:
        return []
    else:
        if array1 == []:
            array1 = [0]
        if array2 == []:
            array2 = [0]
        for i in array1:
            if i == "-":
                n1 = -n1
            else:
                n1 += str(i)
        for i in array2:
            if i == "-":
                n1 = -n1
            n2 += str(i)
    rezn = list(str(int(n1) + int(n2)))
    if rezn[0] == '-':
        rezn.remove('-')
        for i in rezn:
            rez.append(int(i))
        rez[0] = -(rez[0])
    else:
        for i in rezn:
            rez.append(int(i))

    return rez

print(sum_arrays([3, 2, 9], [1, 2]))#, [3, 4, 1])
print(sum_arrays([4, 7, 3], [1, 2, 3]))#, [5, 9, 6])
print(sum_arrays([1], [5, 7, 6]))#, [5, 7, 7])
print(sum_arrays([-3, 4, 2], [3, 4, 4]))#, [2])
print(sum_arrays([], []))# [])
print(sum_arrays([0], []))#, [0])
print(sum_arrays([], [1, 2]))#, [1, 2])
print(sum_arrays([3,2,6,6],[-7,2,2,8]))#,[-3,9,6,2])