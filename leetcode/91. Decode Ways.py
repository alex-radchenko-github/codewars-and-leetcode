import functools
def numDecodings(s):
    x = functools.reduce(lambda x,y: print(x,y),list(s))
    return x
print(numDecodings("2263"))