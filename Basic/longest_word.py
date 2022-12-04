str = "Hello world i am LONGESTWORD using python IDLE"

print(str.split(' '))
list = str.split(' ') 

max = 0
longest_word = ''

for i in list:
    if(len(i) > max):
        max = len(i)
        longest_word = i

print(max)
print(longest_word)
