s=input()
s=list(s)
print(s)
l=[]
for i in s:
    if(ord(i)>=65 and ord(i)<=90):
        l.append(i)

print(l)
