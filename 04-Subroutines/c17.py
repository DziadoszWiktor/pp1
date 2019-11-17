def rzuckostka():
    import random
    a = random.randrange(1,7)
    return a
x = rzuckostka()
y = rzuckostka()
z = rzuckostka()

print(f'Wyrzucone oczka: {x} {y} {z}')
print(f'Suma oczek: {x+y+z}')
    