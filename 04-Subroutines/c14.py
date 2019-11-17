def wystepuje(Liczba,Tablica):
    for x in Tablica:
        if Liczba==x:
            print(f'Liczba: {Liczba}\nTablica: ',end='')
            for y in Tablica:
                print(y,end=' ')
            print(f'\nRezultat: Podana liczba występuje w tablicy')
        else:
            print(f'Liczba: {Liczba}\nTablica: ',end='')
            for y in Tablica:
                print(y,end=' ')
            print(f'\nRezultat: Podana liczba nie występuje w tablicy')
    
a=int(input('Podaj liczbę: '))
Tab=[15,38,7,23,14]
wystepuje(a,Tab)
            
            

