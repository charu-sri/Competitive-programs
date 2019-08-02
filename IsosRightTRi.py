x1,y1=raw_input('Enter first co-ord: ').split()
x2,y2=raw_input('Enter sec co-ord: ').split()
x3,y3=raw_input('Enter third co-ord: ').split()
x1,y1=[int(x1),int(y1)]
x2,y2=[int(x2),int(y2)]
x3,y3=[int(x3),int(y3)]
a=((x1-x2)**2+(y1-y2)**2)**(0.5)
b=((x2-x3)**2+(y2-y3)**2)**(0.5)
c=((x3-x1)**2+(y3-y1)**2)**(0.5)
if((a>b) and (a>c)):
     if((b==c) and (a==(b**2+c**2)**(0.5))):
          print 'true'
     else:
         print 'false'
elif((b>a) and (b>c)):
        if((a==c) and (b==(a**2+c**2)**(0.5))):
             print 'true'
        else:
           print 'false'
else:
        if((a==b) and (c==(a**2+b**2)**(0.5))):
             print 'true'
        else:
              print 'false'
     
      
    
          
          
      

       
