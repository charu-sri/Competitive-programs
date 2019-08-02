from check_prime import *
num=int(raw_input('enter a num'))
flag=check_prime(num)
if flag==0:
    print 'not prime'
else:
    print 'prime'
