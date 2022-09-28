import re
file = open('chat.txt','r',encoding = 'UTF-8')

line = file.readlines()

line2 = re.findall('[0-9][0-9][0-9][0-9]',line[5])
print(line2)
print("Second Git line")
