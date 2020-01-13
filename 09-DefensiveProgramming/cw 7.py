a=int(input('Podaj wzrost: '))
b=float(input('Podaj wage: '))

assert type(a) == int
assert type(b) == float
assert a in range(150,220)
assert b in range(40.0,150.0)

print(f'BMI:{b/(a**2)}')