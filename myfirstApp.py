template = '{0:10} {1:8} {2:6} {3:6} {4:6} {5:6} {6:6} {7:4}'
sdict={}
def display_menu():
    print ('\nMENU')
    print '1. Add student information'
    print '2. Modify student information'
    print '3. Delete student information'
    print '4. Save student information'
    print '5. Display student information'
    print '6. Quit'

    ch=int(raw_input('enter your choice: '))
    if(ch==1):
        getinfo()
    elif(ch==2):
        id=int(raw_input('Enter student id'))
        modifyRecord(id)
    elif(ch==3):
        id=int(raw_input('Enter student id'))
        deleteRecord(id)
    elif(ch==4):
        save()
    elif(ch==5):
        printInfo()
    elif(ch==6):
        print('Thank You')
        break
    else:
        print('Invalid choice. Try again')
        display_menu()
        
               
def getinfo():
    print ('\nEnter the student details: \n')
    name = raw_input('Name         :')
    sid  = raw_input('Student RN   :')
    cls  = raw_input('Class        :')
    phy  = raw_input('Physics      :')
    chem = raw_input('Chemistry    :')
    math = raw_input('Maths        :')
    eng  = raw_input('English      :')

    student = {}
    student['name'] = name
    student['sid'] = sid
    student['cls'] = cls
    student['phy'] = phy
    student['chem'] = chem
    student['math'] = math
    student['eng'] = eng
    
    sdict[name] = student
    
    #DEBUG Code Starts
    print student
    print sdict
    #DEBUG Code Ends
    
    return 1

               
