Python 2.7 (r27:82525, Jul  4 2010, 07:43:08) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> n=int(input())


Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    n=int(input())
  File "<string>", line 0
    
   ^
SyntaxError: unexpected EOF while parsing
>>> ================================ RESTART ================================
>>> 
test cases2
num4
0
num5
0
>>> ================================ RESTART ================================
>>> 
Enter a number5
1 2 3 4 5 5 4 3 2 1
1 2 3 4     4 3 2 1
1 2 3         3 2 1
1 2             2 1
1                 1
>>> ================================ RESTART ================================
>>> 
test cases1
num4
2
1
0
>>> ================================ RESTART ================================
>>> 
test cases1
num4
1
>>> ================================ RESTART ================================
>>> 
test cases
2
num249
1
num5
1
>>> l=['ear',4,[1,2,3],' ']
>>> l
['ear', 4, [1, 2, 3], ' ']
>>> print l,
['ear', 4, [1, 2, 3], ' ']
>>> print l
['ear', 4, [1, 2, 3], ' ']
>>> l[2]
[1, 2, 3]
>>> l[2][0]
1
>>> l[2][2]
3
>>> l[0][0]
'e'
>>> 
>>> l[3][0]
' '
>>> l[3][4]

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l[3][4]
IndexError: string index out of range
>>> d1={'name': 'ear',
   'num':'4',
    'array':[1,2,3],
    'space':' '}
>>> d1={'name': 'ear',
   'num':4,
    'array':[1,2,3],
    'space':' '}
>>> d1
{'array': [1, 2, 3], 'num': 4, 'name': 'ear', 'space': ' '}
>>> d1={'name': 'ear','nose','eyes',
   'num':'4',
    'array':[1,2,3],
    'space':' '}
SyntaxError: invalid syntax
>>> d1={'name': 'ear',
   'num':'4',
    'array':[1,2,3],
    'space':' '}
>>> d1['name']
'ear'
>>> d1={'name': ['ear','nose','eyes'],
   'num':'4',
    'array':[1,2,3],
    'space':' '}
>>> d1['rank']

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d1['rank']
KeyError: 'rank'
>>> d1['name']
['ear', 'nose', 'eyes']
>>> d1['rank']=1
>>> d1
{'array': [1, 2, 3], 'num': '4', 'name': ['ear', 'nose', 'eyes'], 'rank': 1, 'space': ' '}
>>> d1.keys()
['array', 'num', 'name', 'rank', 'space']
>>> d1.values()
[[1, 2, 3], '4', ['ear', 'nose', 'eyes'], 1, ' ']
>>> d1.items()
[('array', [1, 2, 3]), ('num', '4'), ('name', ['ear', 'nose', 'eyes']), ('rank', 1), ('space', ' ')]
>>> for key in d1.keys():
	print key+'.....>'+str(d1[key])

	
array.....>[1, 2, 3]
num.....>4
name.....>['ear', 'nose', 'eyes']
rank.....>1
space.....> 
>>> d1[0]

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d1[0]
KeyError: 0
>>> ================================ RESTART ================================
>>> 
enter a num5

Traceback (most recent call last):
  File "C:/Users/Charu Srivastva/Desktop/python exp/check_primeCall.py", line 3, in <module>
    flag=check_prime(num)
TypeError: 'module' object is not callable
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
enter a num5

Traceback (most recent call last):
  File "C:/Users/Charu Srivastva/Desktop/python exp/check_primeCall.py", line 3, in <module>
    flag=check_prime(num)
TypeError: 'module' object is not callable
>>> ================================ RESTART ================================
>>> 
enter a num5
primr
>>> ================================ RESTART ================================
>>> 
enter a num6
not prime
>>> 
