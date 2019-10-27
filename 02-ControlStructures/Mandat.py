a = int(input("Podaj limit predkosci (km/h): "))
b = int(input("Podaj predkosc pojazdu (km/h):  "))

if b<=60:
    m=(b-a)*5
    print("Mandat (zl): ",m)

if b<=50:
    print("Mandat (zl): 0 ")
    
if b>60:
    n=(b-a)*5*1.5
    print("Mandat (zl): ",n)
    
    
