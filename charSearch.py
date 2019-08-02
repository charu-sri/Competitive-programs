s=raw_input('Enter a string ')
c=raw_input('Enter a character to search ')
l=len(s)
i=list(s)
p=0
for j in range(l):
    if(c==i[j]):
        print (j)
        p=p+1
if(p==0):
    print ('Given character is not present in the given string')
