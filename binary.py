t=raw_input('test cases')
t=int(t)

while(t!=0):
    n=raw_input('num')
    n=int(n)
    while(n!=0):
        r=n%2
        n=n/2
    print r
    t=t-1
    
