def clean_string(s):
    rez = []
    for i in s:
        if i != "#":
            rez.append(i)
        else:
            if rez == []:
                continue
            else:
                rez.pop(-1)
    return ''.join(rez)

print(clean_string('abc#d##c'))#, "ac")
print(clean_string('abc####d##c#'))#, "" )
print(clean_string("#######"))#, "" )
print(clean_string(""))#, "" )