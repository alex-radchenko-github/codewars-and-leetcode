def myAtoi(s):
    s = s.lstrip().split(" ")
    if s[0][0] == '-':
        x = s[0].split("-")
        return -2147483648 if -(int(x[1])) < -2**31 else -(int(x[1]))
    elif s[0][0] != '-':
        #print(int(float(s[0])))
        if str(int(float(s[0]))).isdigit():
            return 2147483648 if int(int(float(s[0]))) > (2**31)-1 else int(int(float(s[0])))
        else:
            return 0

#print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
#print(myAtoi("   -42"))
print(myAtoi("-91283472332"))
print(myAtoi("3.14159"))