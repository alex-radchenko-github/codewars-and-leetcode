lst = [1,3,4,5]
min1 = min(range(len(lst)), key=lst.__getitem__)
max1 = max(range(len(lst)), key = lst.__getitem__)
print(min1)


#2,5,1,3,4,7