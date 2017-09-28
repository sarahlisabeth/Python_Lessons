C:\Users\rawrg>py
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> raw_input()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'raw_input' is not defined
>>> input()
I am Learning at hackerearth
'I am Learning at hackerearth'
>>> print("Guido")
Guido
>>> Print('"Guido"')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined
>>> print('"Guido"')
"Guido"
>>>>>> beautiful_number = input("tell me a beautiful numer ")
tell me a beautiful numer 25
>>> print(beautiful_number)
25
>>> print(Beautiful_number)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Beautiful_number' is not defined
>>> print("5"*6)
555555
>>> print(beautiful_number*6)
252525252525
>>> print(5,6,7)
5 6 7
>>> print(567)
567
>>> print(5 6 7)
  File "<stdin>", line 1
    print(5 6 7)
            ^
SyntaxError: invalid syntax
>>>
>>> print('LOVE',30,82.2)
LOVE 30 82.2
>>> print('LOVE'.30,82.2,sep=',')
  File "<stdin>", line 1
    print('LOVE'.30,82.2,sep=',')
                  ^
SyntaxError: invalid syntax
>>> print('LOVE', 30, 82.2, sep= ',')
LOVE,30,82.2
>>> print('LOVE, 30, 82.2, sep= ', ')
  File "<stdin>", line 1
    print('LOVE, 30, 82.2, sep= ', ')
                                    ^
SyntaxError: EOL while scanning string literal
>>> print('LOVE', 30, 82.2, sep= ', ')
LOVE, 30, 82.2
>>>>>> decimal = input("give me a decimal value")
give me a decimal value12.5
>>> print(decimal)
12.5
>>> randomness = input("input randomness: ")
input randomness: wjehfwuepu2h
>>> print(randomness)
wjehfwuepu2h
>>> print(randomness + " heyyy")
wjehfwuepu2h heyyy
>>> print(randomness + beautiful_number +decimal)
wjehfwuepu2h2512.5
>>> print(randomness - decimal)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> print(random * decimal)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'random' is not defined
>>> print(randomness * decimal)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> print(randomness * beautiful_number)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>>
>>> for i in "python": print(i)
...
p
y
t
h
o
n
>>> for i in "python":
... print(i)
  File "<stdin>", line 2
    print(i)
        ^
IndentationError: expected an indented block
>>> for i in "python":
...     print(i)
...
p
y
t
h
o
n
>>> for I in "Sarah":
...     print(i)
...
n
n
n
n
n
>>> for I in "Sarah":
...     print(I)
...
S
a
r
a
h
>>> print("hey", 'ho', "let's go", sep=',', end='!!\n')
hey,ho,let's go!!
>>>
