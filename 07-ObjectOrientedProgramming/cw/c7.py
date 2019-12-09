class student():
    licznik=100000;
    
    def __init__(self,imie,nazwisko,kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kierunek = kierunek
        self.nralbum = student.licznik
        student.licznik += 1
    def __str__(self):
        return f'{self.imie},{self.nazwisko},({str(self.nralbum)}),{self.kierunek}'

a = student('mark','white','inf')
b = student('josh','turner','eco')
c = student('frank','philips','HR')
print(a)
print(b)
print(c)
        