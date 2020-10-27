def convert(s,numRows):
    row = 0
    d = 1
    data = [""] * numRows
    for x in s:
        if d == 0:
            data[d] = data[d] + x
            d += 1
        elif d == 1:
            data[d] = data[d] + x
            d += 1
        elif d == 2:
            data[d] = data[d] + x
            d -= 1
    return data


print(convert("PAYP", 3), "PINALSIGYAHRPI")
print(convert("PAYPALISHIRING", 3) == "PINALSIGYAHRPI")

#data = [""] * numRows
#for c in s:
#    data[row] = data[row] + c
#    if row == 0:
#        d = 1
#    elif row == numRows - 1:
#        d = -1
#    row = row + d