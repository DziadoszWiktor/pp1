class x():
    
    def __init__(self):
        self.name = "UEK"
        self.full_name = 'Uniwersytet Ekonomiczny w Kkakowie'
        
    def print_name(self):
        print(self.name)
        print(self.full_name)
        
    def set_name(self,new_name):
        self.name = new_name
        print(f'imie zmienione to: {new_name}')
    
    def full_name(self):
        print(self.full_name)
        
    def set_fullname(self,new_fullname):
        self.full_name = new_fullname
        print(f'imie pelne zmienione to: {new_fullname}')
        
        
x= x()
x.print_name()
x.set_name('AGH')
x.set_fullname('Akademia Gorniczo Hutnicza')