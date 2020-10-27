def subdomainVisits(cpdomains):
    rez2 = {}
    rez3 = []
    for i in cpdomains:
        x1 = i.split(" ")
        x2 = x1[1].split(".")
        for i1 in range(len(x2)):
            if ".".join(x2[i1:]) in rez2:
                rez2[".".join(x2[i1:])] = int(rez2[".".join(x2[i1:])]) + int(x1[0])
            else:
                rez2[".".join(x2[i1:])] = int(x1[0])

    for i in rez2:
        rez3.append(str(rez2[i]) + " " + i)

    return rez3

#    rez = []
#    rez2 = {}
#    rez3 = []
#    for i in cpdomains:
#        x1 = i.split(" ")
#        x2 = x1[1].split(".")
#        for i1 in range(len(x2)):
#            rez.append([[".".join(x2[i1:])], int(x1[0])])
#    for i in rez:
#        if i[0][0] in rez2:
#               rez2[i[0][0]] = rez2[i[0][0]] + i[1]
#        else:
#            rez2[i[0][0]] = i[1]
#    for i in rez2:
#        rez3.append(str(rez2[i]) + " " + i)
#
#    return rez3, rez2, rez
#print(subdomainVisits(["9001 discuss.leetcode.com"]))
print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))