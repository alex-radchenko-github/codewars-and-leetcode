def validMountainArray(A):
    rez = []
    count_n = 0
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            rez.append(True)
        elif A[i-1] < A[i]:
            count_n +=1
        elif A[i-1] < A[i]:
            return False
print(validMountainArray([0,3,2,1]))