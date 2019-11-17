def suma(N):
    if N>0:
        return N + suma(N-1)
    else:
        return 0
    
print('Obliczanie sumy liczb z przedziału od 1 do N')
x=int(input('Podaj liczbę N: '))
print(f'Suma liczb z przedziału <1,{x}> wynosi: {suma(x)}')