import statistics

x = statistics.mean([21600,4350,3920,5590,3250,4010])
print(f'Srednia wynagrodzen jest : {x} zl')

y = statistics.median([21600,4350,3920,5590,3250,4010])
a=int(y)
print(f'Mediana wynagrodzen jest : {a} ')

z = statistics.pvariance([21600,4350,3920,5590,3250,4010])
print(f'Odchylenie standardowe  wynagrodzen jest : {round(z,2)}')