import re
kom ='wtorek -23C, sroda -17C, czwartel -25C'
c=re.findall('\d{2}',kom)
suma = 0
for x in c:
    suma+=int(x)
sr = round(suma/len(c),2)
print('Srednia temperatura jest: = ', sr)