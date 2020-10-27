def solve(a,b):
    return "".join([c for c in a if not c in b]+[c for c in b if not c in a])
print(solve("xyab","xzca"))#,"ybzc")
print(solve("xyabb","xzca"))#,"ybbzc")
print(solve("abcd","xyz"))#,"abcdxyz")
print(solve("xxx","xzca"))#,"zca")