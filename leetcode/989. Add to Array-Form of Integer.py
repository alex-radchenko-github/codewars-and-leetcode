def addToArrayForm(A,K):
    rez = []
    a_int = ""
    for i in A:
        a_int += str(i)
    for i in list(str(int(a_int) + K)):
        rez.append(int(i))
    return rez
print(addToArrayForm([1,2,0,0], 34))