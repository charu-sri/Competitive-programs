Python 2.7 (r27:82525, Jul  4 2010, 07:43:08) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s='cosmopoliton'
>>> type s
SyntaxError: invalid syntax
>>> type(s)
<type 'str'>
>>> s[0]
'c'
>>> s[0:1]
'c'
>>> s[0:5]
'cosmo'
>>> s[5]
'p'
>>> s[5]='P'

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s[5]='P'
TypeError: 'str' object does not support item assignment
>>> //char of strings cannot be replaced
SyntaxError: invalid syntax
>>> /char of strings cannot be replaced
SyntaxError: invalid syntax
>>> s[:]
'cosmopoliton'
>>> s[::1]
'cosmopoliton'
>>> s[::2]
'csooio'
>>> s[::3]
'cmot'
>>> s[-1]
'n'
>>> s[-1:-3]
''
>>> s[-3:-1]
'to'
>>> s[-4,-1]

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s[-4,-1]
TypeError: string indices must be integers, not tuple
>>> s[-4:-1]
'ito'
>>> s[-4]
'i'
>>> s[-4:]
'iton'
>>> s[::-1]
'notilopomsoc'
>>> s1=s
>>> s1
'cosmopoliton'
>>> s2=s[::-1]
>>> s2
'notilopomsoc'
>>> s3=s[0:5:-1]
>>> s3
''
>>> s3=s[0:5][::-1]
>>> s3
'omsoc'
>>> s3+'guilt'
'omsocguilt'
>>> s3+s2
'omsocnotilopomsoc'
>>> s.upper()
'COSMOPOLITON'
>>> `s.lower()
SyntaxError: invalid syntax
>>> s.lower()
'cosmopoliton'
>>> s1=s.upper()
>>> s1
'COSMOPOLITON'
>>> s1.lower()
'cosmopoliton'
>>> s.capitalize()
'Cosmopoliton'
>>> lens(s)

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    lens(s)
NameError: name 'lens' is not defined
>>> len(s)
12
>>> len(s[0:5][::-1])
5

>>> s.split()
['cosmopoliton']
>>> s.split(,)
SyntaxError: invalid syntax
>>> s
'cosmopoliton'
>>> l=s.split()
>>> l
['cosmopoliton']
>>> l[5]

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    l[5]
IndexError: list index out of range
>>> l
['cosmopoliton']
>>> l(5)

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    l(5)
TypeError: 'list' object is not callable
>>> l=s.split('')

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    l=s.split('')
ValueError: empty separator
>>> l=list(s)
>>> l
['c', 'o', 's', 'm', 'o', 'p', 'o', 'l', 'i', 't', 'o', 'n']
>>> l[5]
'p'
>>> l[5]='P'
>>> l
['c', 'o', 's', 'm', 'o', 'P', 'o', 'l', 'i', 't', 'o', 'n']
>>> s4=".join(l)
SyntaxError: EOL while scanning string literal
>>> s4=''.join(l)
>>> s4
'cosmoPoliton'
>>> s5='_'.join(l)
>>> s5
'c_o_s_m_o_P_o_l_i_t_o_n'
>>> s6=s5.split('_')
>>> s6
['c', 'o', 's', 'm', 'o', 'P', 'o', 'l', 'i', 't', 'o', 'n']
>>> s7=s.split('o')
>>> s7
['c', 'sm', 'p', 'lit', 'n']
>>> s8='O'.join(s7)
>>> s8
'cOsmOpOlitOn'
>>> s9=s+' '
>>> s9
'cosmopoliton '
>>> s9.strip()
'cosmopoliton'
>>> s9=s+'   '
>>> s9
'cosmopoliton   '
>>> s9.strip()
'cosmopoliton'
>>> for c in s:
	print c

	
c
o
s
m
o
p
o
l
i
t
o
n
>>> for m in s:
	print m

	
c
o
s
m
o
p
o
l
i
t
o
n
>>> 'o' in s
True
>>> 'z' in s
False
>>> 'cosmo' in  s
True
>>> 'lop' in s[::-1]
True
>>> s.index('o')
1
>>> s.find('0')
-1
>>> s.find('o')
1
>>> s.find(0,10,'mop')

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.find(0,10,'mop')
TypeError: slice indices must be integers or None or have an __index__ method
>>> s.find('mop',0,10)
3
>>> print [pos for pos, char in enumerate(s) if char == 'o']
[1, 4, 6, 10]
>>> 
