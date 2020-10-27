def missing(s):
    temp_arr = []
    return len(s)/4

print(missing("123567"))#,4)
print(missing("899091939495"))#,92)
print(missing("9899101102"))#,100)
print(missing("599600601602"))#,-1)
print(missing("8990919395"))#,-1)
print(missing("998999100010011003"))#,1002)
print(missing("99991000110002"))#,10000)
print(missing("979899100101102"))#,-1)
print(missing("900001900002900004900005900006"))#,900003)