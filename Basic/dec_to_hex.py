#wap to enter a decimal number and convert it into hex

dec_num = int(input("Enter Decimal Number - "))

s=''

#list = ['a', 'b', 'c', 'd', 'e', 'f']

while(dec_num > 0):
    new = dec_num % 16
    #if new in range(9, 16):
    #    s = list[new - 16] + " " + s
    if new > 9:
        s = chr(55 + new) + " " + s
    else:
        s = str(new)+ " " + s 
    dec_num = dec_num // 16
    

print(s)
