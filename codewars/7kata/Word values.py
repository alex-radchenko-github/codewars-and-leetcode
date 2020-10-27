def name_value(my_list):
    rez = []
    al = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(len(my_list)):
        rez2 =[]
        for i1 in my_list[i]:
            if i1 == " ":
                continue
            else:
                rez2.append(al.index(i1)+1)
        rez.append(sum(rez2) * (i+1))
    return rez
print(name_value(["abc","abc","abc","abc"]))#,[6,12,18,24])
print(name_value(["codewars","abc","xyz"]))#,[88,12,225])
print(name_value(["abc abc","abc abc","abc","abc"]))#,[12,24,18,24]