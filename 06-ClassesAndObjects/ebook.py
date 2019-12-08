class ebook:
    
    def __init__(self,tytyul,autor,liczbastron):
        self.tytul = tytul
        self.autor = autor
        self.liczbastron = liczbastron
        self.stronaczytana = 0
        self.open = 0
        
    def kopen(self):
        self.open = 1
        self.stronaczytana = 1
    def kclosed(self):
        self.open = 0
        
    def nx(self):
        if self.open:
            if self.liczbaczytana < self.liczbastron:
                self.stronaczytana += 1
        else:
            print('ebook off')
    def pr(self):
        if self.open:
            if self.stronaczytana > 2:
                stronzczytana -= 1
        else:
            print('ebook off')
            
    def show(self):
         print(f'Tytul:{self.tytul}\nAutor:{self.autor}\nLiczba stron:{self.strony}\nStrona otwarta:{self.stronaczytana}')
