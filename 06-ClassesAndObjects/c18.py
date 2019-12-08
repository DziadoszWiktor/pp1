class kostka():
    
    def __init__(self):
        self.k = 0
        
    def rzut(self):
        import random
        self.k = random.randrange(1,7)
        return self.k

x = kostka()
y = kostka()
z = kostka()

x.rzut()
