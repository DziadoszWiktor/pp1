class tv():
    
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.channels = []
        
    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on  = False
        
    def set_channel(self,channel):
        self.channel = channel
    
    def set_channels(self,channels_list):
        channel =''
        
    
    def show_status(self):
        if self.is_on == True:
            print(f'is on, kanal: {self.channel}')
        else:
            print(f'is off')
            
    def show_channels():
        

t= tv()
t.on()
t.set_channel(5)
t.show_status()


        
        
        