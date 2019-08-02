a=raw_input('Enter first num ')
b=raw_input('Enter second num ')
a=int(a)
b=int(b)
for i in range(1,a+1):
    if(a%i==0 and b%i==0):
        gcd=i
        i=i+1

lcm=(a*b)/gcd
print 'gcd of',a,' and ',b,' is ',gcd
print 'lcm of',a,' and ',b,' is ',lcm
    
