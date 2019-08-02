str1='1234'
str2='1324'

'''

c=0
if( len(str1) != len(str2)):
    print('not anagram')
else:
    for i in str1:
        for j in str2:
            if i==j:
                c=c+1

    if c==len(str1):
        print('anagram '+str(c))
    else:
        print('not anagram '+str(c))

ls1=list(str1);ls2=list(str2)
for elem in ls1:
    if elem in ls2:
        ls1.remove(elem);ls2.remove(elem)
if ls1==ls2: print('anagram')
else: print('not anagram')

import os
#print(os.walk('.'))
for elem in os.
    print(elem)
                
'''

str1='335669'
l=list(str1)
l = list(map(int, l))
for i in range(len(str1)):
    if ((l[i]%2!=0 and i%2==0) or (l[i]%2==0 and i%2==0)):
        temp=l[i+1]
        l[i+1]=l[i]
        l[i]=temp

print(l)
        
        
        
       
