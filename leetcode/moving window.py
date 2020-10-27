def moving_window(arr, n):
    for i in range(len(arr)+1-n):
        print(arr[i:i+n])

print(moving_window([1,2,3,3,3,6,7,8], 2))
print(moving_window([1,2,3,3,3,6,7,8], 3))
print(moving_window([1,2,3,3,3,6,7,8], 4))
print(moving_window([1,2,3,3,3,6,7,8], 5))
print(moving_window([1,2,3,3,3,6,7,8], 7))