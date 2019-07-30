def gradingStudents(grades):
    new_grade=[]
    n=len(grades)
    for i in range(n):
        c=grades[i]
        while(c%5!=0):
            c=c+1
        if(c>=40):
            if(c-grades[i]<3):
                new_grade.append(c)
            elif(c-grades[i]>=3):
                new_grade.append(grades[i])
        else:
            new_grade.append(grades[i])
    return new_grade
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(raw_input().strip())

    grades = []

    for _ in xrange(grades_count):
        grades_item = int(raw_input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
