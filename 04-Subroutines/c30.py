import random
def los():
    return random.randrange(1,51)

tab=[]
p=0
np=0
for x in range(0,1001):
    tab.append(los())
for x in tab:
    if x%2==0:
        p+=1
    else: np+=1
print(f'Dla 1000 liczb losowych z przedziału <1,50>:\nLiczby parzyste: {round((p/len(tab))*100,2)}%\nLiczby nieparzyste: {round((np/len(tab))*100,2)}%')

