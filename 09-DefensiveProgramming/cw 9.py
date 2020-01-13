import math 
a = int(input('Podaj a: '))

assert a >=0, 'liczba ujemna'

print(f'{math.sqrt(a)}')

try:
    number = float(input('Podac numer: '))
    print(f'{math.sqrt(number)}')
except:
    print('Liczba ujemna')

