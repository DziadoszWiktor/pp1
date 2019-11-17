Imiona=['Janek','Ania','Wojtek','Zosia']
def jestImie(x,y):
    if x in Imiona:
        return 1
    else:
        return 0
    
Imie=input('Podaj imię: ')

if jestImie(Imie,Imiona)==1:
    print('Imię znajduje się w wykazie.')
else:
    print('Imienia nie ma w wykazie.')