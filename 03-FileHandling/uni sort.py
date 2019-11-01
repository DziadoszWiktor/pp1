import re
uni=[]
ps=[]
with open('universities.txt','r') as file:
    for x in file:
        uni.append(x)
file.close()

uni.sort()
with open('universities.txt','w') as file:
    for i in uni:
        file.write(i)
file.close()