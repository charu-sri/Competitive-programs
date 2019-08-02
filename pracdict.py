Python 2.7 (r27:82525, Jul  4 2010, 07:43:08) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print(":".join("Python"))
P:y:t:h:o:n
>>> string="12345"
>>> print(' '.join(reversed(string)))
5 4 3 2 1
>>> print(reversed(string))
<reversed object at 0x00000000022D5BA8>
>>> word="guru99 career guru99"
>>> print(word.split(' '))
['guru99', 'career', 'guru99']
>>> x=("guru99",20,"edu")
>>> (comp, emp, pro)=x
>>> print(comp)
guru99
>>> print(emp)
20
>>> print(pro)
edu
>>> string[::-1]
'54321'
>>> a={'x':100,'y':200}
>>> b=list(a.items())
>>> print b
[('y', 200), ('x', 100)]
>>> a.all()

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.all()
AttributeError: 'dict' object has no attribute 'all'
>>> b.all()

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b.all()
AttributeError: 'list' object has no attribute 'all'
>>> a.max()

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.max()
AttributeError: 'dict' object has no attribute 'max'
>>> dict={'tim':18,"charlie':12,'tiffany':22,'robert':25}
      
SyntaxError: EOL while scanning string literal
>>> dict={"tim":18,"charlie":12,"tiffany":22,"robert":25}
>>> boys={"tim":18,"charlie":12,"robert":25}
>>> girls={"tiffany":22}
>>> for key in boys.keys():
	if key in dict.keys():
		print true
	else:
		print false

		

Traceback (most recent call last):
  File "<pyshell#27>", line 3, in <module>
    print true
NameError: name 'true' is not defined
>>> for key in boys.keys():
	if key in dict.keys():
		print True
	else:
		print False

		
True
True
True
>>> a=xrange(1,10000)
>>> print(a)
xrange(1, 10000)
>>> print(type(a))
<type 'xrange'>
>>> print(getsizeof(a))

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(getsizeof(a))
NameError: name 'getsizeof' is not defined
>>> print(sizeof(a))

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(sizeof(a))
NameError: name 'sizeof' is not defined
>>> a=xrange
>>> a=xrange(1,6)
>>> print(a[2:5])

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(a[2:5])
TypeError: sequence index must be integer, not 'slice'
>>> a=range(1,6)
>>> print(a[2:5])
[3, 4, 5]
>>> import sys
>>> a=xrange(1,10000)
>>> print(getsizeof(a))

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(getsizeof(a))
NameError: name 'getsizeof' is not defined
>>> print(sys.getsizeof(a))
32
>>> print(sys.getsizeof(a))
32
>>> a=range(1,10000)
>>> print(sys.getsizeof(a))
80056
>>> 
