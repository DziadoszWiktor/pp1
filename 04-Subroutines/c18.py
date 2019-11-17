def silnia(x):
    if x==0 or x==1:
        return 1
    if x > 1:
        return x * silnia(x-1)
    
print(f'5! = {silnia(5)}')