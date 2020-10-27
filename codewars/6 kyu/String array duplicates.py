def dup(arry):
    rez_rez = []
    for i1 in arry:
        rez = [list(i1)[0]]
        for i in range(1, len(list(i1))):
            if list(i1)[i] == list(i1)[i-1]:
                continue
            else:
                rez.append(list(i1)[i])
        rez_rez.append("".join(rez))
    return rez_rez

print(dup(["ccooddddddewwwaaaaarrrrsssss", "piccaninny", "hubbubbubboo"]))#, ['codewars', 'picaniny', 'hubububo'])
