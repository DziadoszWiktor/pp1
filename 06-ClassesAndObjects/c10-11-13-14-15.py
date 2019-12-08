class tv():
    
    def __init__(self):
        self.int = False
        self.chann = 1
        self.tab = []
        self.vol = 0
        
    def on (self):
        self.int = True
    
    def off(self):
        self.int = False
        
    def chan(self,chan):
        self.chann = chan
    
    def tabchan(self,lista):
        self.tab = lista
    
    def volup(self):
        self.vol =+10
    def voldown(self):
        if self.vol>0:
            self.vol=-10
    
    def show(self,v):
        if self.int == True:
            print(f'\n-TV is on. \nVolume:{self.vol} \n  channel: {self.chann},{v[self.chann-1] }')
        else:
            print('\n-TV is off')
    
    def showchan(self):
        print('Kanaly:')
        for x in range (len(self.tab)):
            print(f' {x+1}.{self.tab[x]}',end='')

v = ['TVP1','TVP2','TVN','POLSAT','TVN Turbo']

t = tv()
t.on()
t.chan(3)
t.tabchan(v)
t.volup()
t.show(v)
t.showchan()
t.chan(4)
t.show(v)
t.showchan() 