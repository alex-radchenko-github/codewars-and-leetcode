def base_finder(seq):
    rez = []
    for i in seq:
        rez.append(int(i))
    rez2 = list(range(rez[0], rez[-1] + 1))
    if rez2 == rez:
        return len(rez)
    for i in range(len(rez2)):
        if rez2[i] == rez[i]:
            continue
        else:
            return i+1
            break
print(base_finder(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']))#, 10)
print(base_finder(['1', '2', '3', '4', '5', '6', '10', '11', '12', '13']))#, 7)
