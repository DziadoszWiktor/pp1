x = int(input("Wpisz x: "))
y = int(input("Wpisz y: "))

txt = "P : ({},{})"
print(txt.format(x,y))

if x>0 and y>0:
    print("P nalezy do czwiartki nr1 ")
    
if x>0 and y<0:
    print("P nalezy do czwiartki nr4 ")
    
if x<0 and y>0:
    print("P nalezy do czwiartki nr2 ")
    
if x<0 and y<0:
    print("P nalezy do czwiartki nr3 ")
    

    
