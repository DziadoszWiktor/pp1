class music():
    
    def __init__(self,artist,title,album,year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year
        t = [self.artist,self.title,self.album,self.year]
        
        
    def __str__(self):
        return f'''
Wykonawca: {self.artist}
Tytul:     {self.title}
Album:     {self.album}
Rok:       {self.year}'''
    
u = music('...','...','...','...')
print(u)
    