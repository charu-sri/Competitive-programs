n=raw_input('Enter a num: ')
print 'you have entered: '+ n
n=int(n)
prime=True
if((n==0) or (n==1)):
    print 'undermined'
elif(n==2):
    print 'prime'
else:

    for i in range(2,n):
        if(n%i==0):
            prime=False
            break

if(prime==True):
    print 'num is prime'

else:
    print 'not prime'
    
