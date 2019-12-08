class bank:
    
    def __init__(self,n):
        self.n = n
        self.balans = 0
        
    def wplac(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance -= amount
        else:
            print('Niewystarczająca ilość środków na rachunku')
   
   def status(self):
        print(f'Numer rachunku: {self.n}\nSaldo: {self.balance} zł') 
    
    
m = bank("12 3456 5555 9090 1111 0000 7722")
m.status()
m.wplac(25.30)
m.status()
m.withdraw(31.70)
m.status()
m.withdraw(14)
m.status()