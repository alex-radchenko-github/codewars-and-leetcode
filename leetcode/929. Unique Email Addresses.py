def numUniqueEmails(emails):
    rez = []
    for i in emails:
        t1 = i.split("@")
        t2 = t1[0].split("+")
        t3 = "".join(t2[0].split("."))
        rez.append(t3 + "@" + t1[1])
    return len(set(rez))


print(numUniqueEmails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
