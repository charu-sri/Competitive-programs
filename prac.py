Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d1={a:'1',b:'1,2',c:'1,2,3'}
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    d1={a:'1',b:'1,2',c:'1,2,3'}
NameError: name 'a' is not defined
>>>  d1={'a':'1','b':'1,2','c':'1,2,3'}
SyntaxError: unexpected indent
>>> d1={'a':'1','b':'1,2','c':'1,2,3'}
>>> d1
{'a': '1', 'b': '1,2', 'c': '1,2,3'}
>>> d1.items()
dict_items([('a', '1'), ('b', '1,2'), ('c', '1,2,3')])
>>> d2={}
>>> d2
{}
>>> for x,y in d1.items()
SyntaxError: invalid syntax
>>> d1.iteritems()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d1.iteritems()
AttributeError: 'dict' object has no attribute 'iteritems'
>>> d1={'a':1,'b':1,'c':1,'d':2,'e':2,'f':3}
>>> d1.items()
dict_items([('a', 1), ('b', 1), ('c', 1), ('d', 2), ('e', 2), ('f', 3)])
>>> d2.items()
dict_items([])
>>> for x,y in d1.items():
	if (d2.items()==y):
		d2[y]=x

		
>>> d2.items()
dict_items([])
>>> for x,y in d1.items():
	if (d2.items()==y):
		d2[y].append(x)
	else:
		d2[y]=x

		
>>> d2
{1: 'c', 2: 'e', 3: 'f'}
>>> for x,y in d1.items():
	if (d2.items()==y):
		d2[y].append(x)
		print(d2)
	else:
		d2[y]=x
		print(d2)

		
{1: 'a', 2: 'e', 3: 'f'}
{1: 'b', 2: 'e', 3: 'f'}
{1: 'c', 2: 'e', 3: 'f'}
{1: 'c', 2: 'd', 3: 'f'}
{1: 'c', 2: 'e', 3: 'f'}
{1: 'c', 2: 'e', 3: 'f'}
>>> d1.item()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d1.item()
AttributeError: 'dict' object has no attribute 'item'
>>> for x,y in d1.items():
	print(x)
	print(y)

	
a
1
b
1
c
1
d
2
e
2
f
3
>>> for x,y in d1.items():
	d2[y].append(x)

	
Traceback (most recent call last):
  File "<pyshell#33>", line 2, in <module>
    d2[y].append(x)
AttributeError: 'str' object has no attribute 'append'
>>> for x,y in d1.items():
	d2[y].join(x)

'a'
'b'
'c'
'd'
'e'
'f'
>>> d2.items()
dict_items([(1, 'c'), (2, 'e'), (3, 'f')])
>>> d2={}
>>> d2
{}
>>> 
