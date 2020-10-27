def move_zeros(array):
    rez = []
    ind = []
    for i in range(len(array)):
        if array[i] == 0 and type(array[i]) is int or type(array[i]) is float:
            ind.append(i)
        else:
            rez.append(array[i])
    for i in range(len(ind)):
        rez.append(0)
    return rez
print(move_zeros([0.0,0,1,None,2,False,1,0]))