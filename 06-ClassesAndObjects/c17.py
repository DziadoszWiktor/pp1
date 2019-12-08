class ulamek():
    
    def __init__(self,licznik,mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
        
    def show(self):
        print(f'{self.licznik}/{self.mianownik}')
        
u  = ulamek(2,5)
u.show()
        
        