Python 2.7 (r27:82525, Jul  4 2010, 07:43:08) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fd=opem('C:\Python27\fileops\rhyme.txt','r')

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    fd=opem('C:\Python27\fileops\rhyme.txt','r')
NameError: name 'opem' is not defined
>>> fd=open('C:\Python27\fileops\rhyme.txt','r')

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    fd=open('C:\Python27\fileops\rhyme.txt','r')
IOError: [Errno 22] invalid mode ('r') or filename: 'C:\\Python27\x0cileops\rhyme.txt'
>>>  fd=open(r'C:\Python27\fileops\rhyme.txt','r')
 
  File "<pyshell#2>", line 1
    fd=open(r'C:\Python27\fileops\rhyme.txt','r')
   ^
IndentationError: unexpected indent
>>> fd=open(r'C:\Python27\fileops\rhyme.txt','r')

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    fd=open(r'C:\Python27\fileops\rhyme.txt','r')
IOError: [Errno 2] No such file or directory: 'C:\\Python27\\fileops\\rhyme.txt'
>>> fd=open(r'C:\Python27\fileops\rhymes.txt','r')
>>> fd
<open file 'C:\Python27\fileops\rhymes.txt', mode 'r' at 0x0000000002C145D0>
>>> s=fd.read()
>>> s
'Twinkle Twinkle little star\nhow i wonder what you are\nup above the world so high\nlike a diamond in the sky\n\njohny johny yes papa\neating sugar no papa\ntelling a lie no papa\nopen your mouth ha ha ha\n\njingle bell jingle bell\njingle all the way\noh what fun it is to ride\nin a one horse open slay\nhey..\n\n'
>>> fd.close()
>>> fd=open(r'C:\Python27\fileops\rhymes.txt','r')
>>> s=fd.readline()
>>> s
'Twinkle Twinkle little star\n'
>>> fd.readline()
'how i wonder what you are\n'
>>> fd.readline()
'up above the world so high\n'
>>> fd.readlines(2)
['like a diamond in the sky\n', '\n', 'johny johny yes papa\n', 'eating sugar no papa\n', 'telling a lie no papa\n', 'open your mouth ha ha ha\n', '\n', 'jingle bell jingle bell\n', 'jingle all the way\n', 'oh what fun it is to ride\n', 'in a one horse open slay\n', 'hey..\n', '\n']
>>> fd.tell()
315L
>>> fd.seek(0)
>>> fd.tell()
0L
>>> fd.readline()
'Twinkle Twinkle little star\n'
>>> fd.seek(200)
>>> fd.readline()
'a ha\n'
>>> fd.close()
>>> fd=open(r'C:\Python27\fileops\test.txt','w')
>>> #r represents raw string, to tell the computer that there is no escape sequence in the path
>>> #book: Learning Python 5th ed-mark /lutz
>>> s1="i love python"
>>> s2="but m still learning it"
>>> fd.write(s1)
>>> fd.close()
>>> fd=open(r'C:\Python27\fileops\test.txt','r')
>>> fd
<open file 'C:\Python27\fileops\test.txt', mode 'r' at 0x0000000002C144B0>
>>> fd.readline()
'i love python'
>>> fd.readline()
''
>>> fd.see

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    fd.see
AttributeError: 'file' object has no attribute 'see'
>>> fd.seek(0)
>>> fd.readline()
'i love python'
>>> fd=open(r'C:\Python27\fileops\test.txt','w')
>>> fd.write(s2)
>>> fd.close()
>>> fd=open(r'C:\Python27\fileops\test.txt','w')
>>> fd.write(s2)
>>> fd.readline()

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    fd.readline()
IOError: File not open for reading
>>> fd.close()
>>> fd=open(r'C:\Python27\fileops\test.txt','r')
>>> fd.readline()
'but m still learning it'
>>> fd.close()
>>> fd=open(r'C:\Python27\fileops\test.txt','a')
>>> fd.writelines([s1,s2])
>>> fd.close()
>>> 
