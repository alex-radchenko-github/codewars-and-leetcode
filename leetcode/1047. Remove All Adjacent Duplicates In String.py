def removeDuplicates(S):
    rez = []
    for i in S:
        if rez:
            if i == rez[-1]:
                rez.pop()
            else:
                rez.append(i)
        else:
            rez.append(i)
    return "".join(rez)


print(removeDuplicates("abbaca"))