import itertools

def maxLength(arr):
#    for i in list(itertools.combinations(arr, 2)):
#        print("".join(i) == )
#    print(list(itertools.combinations(arr, 2)))
    maxn=[]
    while len(maxn) < 100:
        for i in range(1, len(arr))[::-1]:
            #print(list(range(1, len(arr)+1)[::-1]))
            for i1 in itertools.combinations(arr, 3):
                i1 = "".join(i1)
                print(i1)
                print("".join(sorted(i1)), "".join(sorted(set(i1))))
                if "".join(sorted(i1)) == "".join(sorted(set(i1))):
                    maxn.append(i1)
                    #print(maxn)
                    break
                else:
                    continue

    return maxn


#print(maxLength(["un", "iq", "ue"]))
print(maxLength(["cha","r","act","ers"]))
# print(maxLength(["abcdefghijklmnopqrstuvwxyz"]))
#print(maxLength(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]))
