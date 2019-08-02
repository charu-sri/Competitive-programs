nums=raw_input('Enter a list of numbers ').split(',')
l=list(nums)
u=[]
ui=[]
index=0
size=len(l)
for ele in l:
    if ele in u:
        pass
    else:
        u.append(ele)

for item in u:
    c=0
    for x in l:
        if (item==x):
            c=c+1
    print '{} occurs {} times'.format(item,c)


    
            
    
            
        
        
        
    
    
    
        
        
   
   
