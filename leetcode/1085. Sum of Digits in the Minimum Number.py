def sumOfDigits(A):
    return 0 if sum(int(i) for i in list(str(min(A))))%2 >0 else 1

print(sumOfDigits([99,77,33,66,55]))