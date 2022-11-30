#wap to enter a decimal number and convert it into binary

dec_num = int(input("Enter Decimal Number - "))

s=''

while(dec_num > 0):
    new = dec_num % 2
    s = str(new) + s
    dec_num = dec_num // 2

print(s)
