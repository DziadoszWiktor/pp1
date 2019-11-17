def miesiac(x):
    n=['Styczeń','Luty','Marzec','Kwiecień','Maj','Czerwiec','Lipiec','Sierpień','Wrzesień','Październik','Listopad','Grudzień']
    return n[x-1]
m=int(input('Podaj numer miesiąca: '))
print(f'Nazwa miesiąca o numerze {m} to {miesiac(m)}.')
print(f'Nazwa miesiąca o numerze 7 to {miesiac(7)}.')
print(f'Nazwa miesiąca o numerze {9} to {miesiac(9)}.')