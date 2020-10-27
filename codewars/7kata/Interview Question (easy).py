def get_strings(city):
    rez = []
    rez2 = []
    city = city.lower()
    city = list(city)
    for i in city:
        if i != " ":
            rez.append(i + ":" + city.count(i)*"*")
    for i in rez:
        if i not in rez2:
            rez2.append(i)
        else:
            continue
    return ','.join(rez2)
print(get_strings("Chicago"))#, "c:**,h:*,i:*,a:*,g:*,o:*")
print(get_strings("Bangkok"))#, "b:*,a:*,n:*,g:*,k:**,o:*")
print(get_strings("Las Vegas"))#, "l:*,a:**,s:**,v:*,e:*,g:*")