def licenseKeyFormatting(S,K):
    rez_l = ""
    rez = []
    S = S.upper()[::-1]
    t1 = S.split("-")
    t2 = t1
    t3 = "".join(t2)

    ti = ""
    for i in t3:
        if len(ti) !=K:
            ti += i
        elif len(ti) == K:
            rez.append(ti)
            ti = i
    rez.append(ti)
    #rez.insert(0,t1[0])
    for i in rez:
        rez_l += str(i) + "-"
    return rez_l[::-1][1:]
print(licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(licenseKeyFormatting("2-4A0r7-4k", 4))#24A0-R74K