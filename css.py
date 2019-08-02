import sys
msg=[]
N=int(input())
msg1=input()

while N>0 and msg1!=" ":
    msg.append(msg1)
    N=N-1
l=list(msg)
for i in l:
    if i[0][0]=='#':
        if len(i)==3 or len(i)==6:
            all(c in string.hexdigits for c in i[1:len(i)])
            print(i)
