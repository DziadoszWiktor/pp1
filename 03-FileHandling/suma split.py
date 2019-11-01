import re
counter=0
suma=0
with open('numbersinrows.txt','r')as file :
    for x in file:
        tab=re.split(',',x)
        counter+=len(tab)
        for i in tab:
            suma+=int(i)
print('liczby:{}/nSuma:{}'.format(counter,suma))