def fib(n):
    (x,y)=(0,1)
    for i in range(0,n-1):
        (x,y)=(y,x+y)
    return x
a=1
while a<21:
    print(fib(a),end=' ')
    a+=1
