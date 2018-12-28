def myAtoi(str):
    num = "0"
    for i in range(len(str)):
        if str[i].isdigit():
            num += str[i]
        elif str[i] in '+-' and len(num) == 1:
            num = num +str[i]
        elif str[i] != ' ' or len(num) > 1:
            break
    return max(min(int(num),2**31-1),-2**31)

string = '42'
integer = myAtoi(string)
print('Returned Integer is:',integer)