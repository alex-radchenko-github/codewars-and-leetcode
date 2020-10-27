def split_and_add(numbers, n):
    rez = []
    rez1 = []
    count_loop = 0
    while count_loop != n:
        if len(numbers) < 2:
            return numbers
        elif len(numbers[:len(numbers) % 2]) == 0:
            rez.append(numbers[:len(numbers) // 2])
            rez.append(numbers[(len(numbers) // 2):])
        else:
            rez.append(numbers[:len(numbers) // 2])
            rez.append(numbers[(len(numbers) // 2):])
            rez[0].insert(0, 0)
        for i in range(len(rez[1])):
            rez1.append((rez[0][i]) + (rez[1][i]))
        count_loop += 1
        numbers = rez1
        rez1 = []
        rez = []
    return numbers

print(split_and_add([1,2,3,4,5], 2))#, [5,10])
print(split_and_add([1,2,3,4,5], 3))#, [15])
print(split_and_add([15], 3))#, [15])
print(split_and_add([32,45,43,23,54,23,54,34], 2))#, [183, 125])
#print(split_and_add([32,45,43,23,54,23,54,34], 0))#, [32,45,43,23,54,23,54,34])
#print(split_and_add([3,234,25,345,45,34,234,235,345], 3))#, [305, 1195])
#print(split_and_add([3,234,25,345,45,34,234,235,345,34,534,45,645,645,645,4656,45,3], 4))#, [1040, 7712])
#print(split_and_add([23,345,345,345,34536,567,568,6,34536,54,7546,456], 20))#, [79327])