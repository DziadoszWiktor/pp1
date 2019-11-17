def sum(tablica):
    suma=0
    print('Tablica',end=' ')
    for x in tablica:
        print(x, end=' ')
        suma+=x;
    print(f'\nSuma watosci: {suma}')
        
liczby=str(input('podaj liczby: '))
tab=[]

for x in range(0,len(liczby)):
    tab.append(int(liczby[x]))
    
sum(tab)
        
        