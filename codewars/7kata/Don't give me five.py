def dont_give_me_five(start, end):
    rez = []
    for i in list(range(start, end + 1)):
        if "5" in list(str(i)):
            print(i)
        else:
            rez.append(i)
    return len(rez), rez

#print(dont_give_me_five(1,9))#, 8)
#print(dont_give_me_five(4,17))#, 12)

print(dont_give_me_five(109,151))#, 21)