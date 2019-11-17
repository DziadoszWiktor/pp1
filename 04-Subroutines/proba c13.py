def wystepuje(liczba,tablica):
    if liczba in Tab:
        return 1
    else:
        return 0

Tab=[15,38,7,23,14]
l=input('Podaj liczbe: ')
if wystepuje(l,Tab)==1:
    print('Liczba jest w tablicy.')
else:
    print('Liczby nie ma w tablicy.')