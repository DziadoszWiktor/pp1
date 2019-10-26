import math

a = int (input('a'))
b = int (input('b'))
c = int (input('c'))

p = (a+b+c)/2
P = (p-a)*(p-b)*(p-c)

print math.sqrt(P)