import random

x = int(input("Wpisz numer: "))
if x !=0 and x<7:
    print(x)
else:
    print("nie w kostce tekiego numero ")
y = random.randint(1,6)

if x==y:
    print("True ")
else:
    print("False ")