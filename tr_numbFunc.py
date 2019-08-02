Python 2.7 (r27:82525, Jul  4 2010, 07:43:08) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print 'hello world'
hello world
>>> a=15
>>> print a
15
>>> a
15
>>> b=78
>>> a+b
93
>>> a/b
0
>>> a=15
>>> b=16
>>> a/b
0
>>> b/a
1
>>> a/float(b)
0.9375
>>> a>b
False
>>> c=a>b
>>> c
False
>>> n=100
>>> int(100)
100
>>> hex(n)
'0x64'
>>> oct(n)
'0144'
>>> bin(n)
'0b1100100'
>>> n.bit_length
<built-in method bit_length of int object at 0x000000000259AD60>
>>> n.bit_length()
7
>>> int(n,16)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(n,16)
TypeError: int() can't convert non-string with explicit base
>>> int(100,16)

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(100,16)
TypeError: int() can't convert non-string with explicit base
>>> int(str(n),16)
256
>>> str(n)
'100'
>>> int('100',16)
256
>>> int('100',8)
64
>>> int('n',8)

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int('n',8)
ValueError: invalid literal for int() with base 8: 'n'
>>> int(str(n),8)
64
>>> int('100',2)
4
>>> bin('4',10)

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    bin('4',10)
TypeError: bin() takes exactly one argument (2 given)
>>> len(str(n))
3
>>> bin(int('100',16))
'0b100000000'
>>> bin(4)
'0b100'
>>> 
