'''
Tokens
---Tokens are the small unit in the python..

Identifier
-----------
Variable-->

num = 'python'
print (type(num))

functions
def add (a,b):
    print(a+b)

add_(4,5)

class
class details:
      pass

per_1 = details

keywords
----------
-->keywords re already saved in python foe an specificed reason to run..
eg
--
if
else
for
while
return
print

Literals
----------
-->Literals are the datatypes that need to be stored in variables..
num = 90
name = 'pravalli'

operators
-----------
+, -, =,


statements
----------
-->statements are the instructions given to the program...

num = 9
age = 2
if age >= 10:
    print(age)

comments
--------
-->Once comments are open the lines inside will never execute in python file

1single line comments(#)
----------------------
-->used to comment only one line
eg
age = 20
if age >= 10: #this check age is greater or equal
   print(age)

2.multi-line(''' ''', """ """)
-----------------------------
-->used to comment more than one line

variables rules
--------------
-->can't use number at 1st position
-->can't use special chart anywhere
-->can't use space
-->keywords
eg
2num = 90
$num = 89
n um = 78
if = 67

good ways
--------
-->small letters and cap letters, (_) under
eg
--
nUm_1 = 30
Num_1 = 78
teja_garikapati = 90

a = {'name':'teja',
     'AC_num': '44567890987654')
b = ('name':'garikapati',
     'AC num': '32165431656516')
num = 90
print(num)

num_3
print(num_3}
print(num_2)



Datatypes & TypeConversions
--------------------
-->1.Numeric Datatypes
----------
-->Float and interger is called as numeric datatype..

float
----
-->A number which containes ecimal values, we call it as a float datatype
eg
--
price=56.89

interger (int)
-----
-->A normal value without any decimal values
eg
--
num = 89
num_2 = 6
2.String
--------

-->String is a seuence of character that are enclosed in '',"",""""""

-->String is immutable
eg --
any_= 'python is a language'
all_ = 'Ab,.&[)-+'


3.List
------

-->List is a collection of different datatypes
-->and it is represented by [] that are separated by ,
-->inside the list we call it as items
-->list is mutable
eg
--
any_ = [1,'Pyhton',[5,6]]
print(type(any_))

4.Tuple
-------
-->Tuple is a collection of different datatypes that are enclosed in () and those are separated by ,
-->tuple is immutable
eg
--
nums = (1,89.67,'Python',[3,4],[8,9]])

5.Distionary
------------
-->Dictionary is coolection of key:value pairs , keys and value are separatedmbt :
-->key ad value pair is call it as a item
-->and this items are separated by ,
-->Dictionary is represent using {}
-->in key place we can use immutable datatypes
-->in values place we can use any datatype
eg
--
data_ = {1:2,
         'name':Teja',
         (2,3):'tuple'}
    
6.set
-----
-->set is collection uniqe element and set can't allow any douple values inside it.....
-->set is represented by {} and the elements are separated by ,

an = {1,2,3]
print(an)


typeconversion
----------------
float--. int, str

eg
--
price = 45.78
print(int(price))

price = 45.78

-->str()
price = 45.78
con = str(price)
print(type(con))

integer--. float, str

print(float(num))

-->str()
num= 78
con_
= str(num)
print(type(con_))

string--> int, float
eg--> int()
----
do = '3456'
print(int

do =

list --> tuple, string
eg --. tyuple()
nums =[1,2,3,34]
print(tuple(nums))
tuple--> list
eg-->list()
all_ = (5,6,7)
print(list(all_))

set--> tuple, list
eg--> tuple()
all_ = {5,6,7}
print(tuple(all_))

dicitionary --> list
eg --> dict()

details = [(




Strings
--------
 Operations
 -------------
1.Indexing
------------
-->Indexing is used to get char that you looking to access
Types
1.Positive Indexing
------------------
Positive Indexing starts from 0 index
syntax --> print(variable_name[index position])
eg

text = 'python'
print(text[4])

2.Negative Indexing
------------------
Negative index starts from -1 index
syntax -->print(variable_name[ negative index_position])

eg
--
text = 'python'
print(text[-1])



txt = 'python is a programming language'
print(txt[-15])

len()
-----
-->len () is built-in function that is used get number or char


sciling
-------
-->This is used to access the perticular part from the string
syntax -->variable_name[start:end]

eg :-

txt = 'python is a programming language'
print(txt[12:23])

print(txt[12:])

print (txt[:23])

txt = 'madam'
rev = txt[::-1]

upper()
--------

-->used to convert all small char into cap
txt = 'python is a programming language'
print(txt.upper())

lower()
-------
-->used to convert all cap into small
eg
--
txt = 'PYTHON'
print(txt.lower())


index()
----------
-->used to know the index position of an char
syntax--> variable_name.index('substring',start,end)
eg
---
txt = 'Python is a programmin language'
print(txt.index('i',9.18))

replace()
-----------
-->used to replace old substring with new substring
syntax --> variable_name.replace(old,new)
eg
--
txt = 'Python is a programmin language'
print(txt.replace('Python','Java'))


split
------
--> this method is uded separate the string based on the given substring
syntax-->variable_name.split(substring)
eg
--

txt = 'Python is a programming language'
print(txt.split(' '))

count()
-----
-->used to count number of occurrence of an substring
syntax-->variable_name.count('substring')

eg
--
txt = 'Python is a programming language'
print(txt.count('a'))


indexing
---------
Positive -->0
Negative -->1

so = [1,2,3,4,'Python']
print(so[-1][-3])
all_ = [12,[1,'python',[1,4],(78,[6,7])],['java',78]]


print(all_[1][3][1])

data_ = ['Python',[1,2,(98,'Details',[67,8]),(78,'Student')]]
print(data_[1][2][1][2])


len()
-----
-->The function is used to find the number of items present inside list


data_ = ['Python',[1,2,(98,'Details',[67,8]),(78,'Student')]]
print(len(data_))

sciling
-------
-->
eg

data_ = [1,2,3,4,5,6,7]
print(data_[2:6])

eg
--
a = [1,2]
b = [3,4]
print(a+b)

methods
--------
append()
--------
-->append method will add new items into list at last index position
syntax--> variable_name.append(item)

eg

go = [1,2]
print(go)
go.append(3)
print(go)
go.append(4)
print(go)


extend()
-------
--> extend()will add the items into a list at last index position, but it will give each value as one index inside the list
syntax--> variable_name.extend(items)
eg

go = [1,2]

go.extend('python')
print(go)

pop()
------
-->pop() is used to remove items from the list and it will delete based on the index position

syntax--> variable_name.pop(index_position)

eg

m = [1,2,3,4,'python']
m.pop(3)
print(m)

remove()
-------
-->remove () will delete items based on the value given init..
syntam--.variable_name.remove(value)
eg

m = [5,1,2,3,4,'python']
m.remove(5)
print(m)


tuple
------
-->Tuple is collection of different datatypes that separated by, and represented by ()
-->it is immutable
-->we can pass a tuple values and that can be asign to the variables, but should match same number variables and values inside the tuple
eg
--
t = (1, 'python',[3,4],(7,9))
print(t[2])


indexing
eg
--
t = (1, 'python',[3,4],(7,9))
print(t[2])


index()
------
-->if item is not present in thr tuple, itwill raise valueError
eg
---

t = (1, 'Python',[3,4],(7,9))
print(t.index('python'))


len()
---

t = (1, 'Python',[3,4],(7,9))
print(len(t))


max()
---
-->used to find out the max value from the tuple
eg
-----
so = (67,5,89,45)
print(max(so))

min()
-----
--<used to find out the least value from the tuple
eg
---
so = (67,5,89,45)
print(min(so))

count()
--------
-->used to count an item present in the tuple

set
----
-->set is unordered collection of elements
-->no duplicate allowed in the set
-->set is represented by {}
eg
---
nums = {1,2,3,2}
print(nums)


operations
----------
union
----
-->the union () will combine two set into a single set
syntax-->set_1.union(set_2) or set_1 | set_2
eg
----
data_ = {1,2,3,4}
nums ={5,6}
print(data_.union(nums))
print(data_ | nums)


intersection()
------------
-->thid will gives us the common elements from both sets
syntax ---> set_1.intersection(set_2) or set_1 & set_2

difference()
-----------
-->it will display the difference elements from set_1 but not the set_2 elements
syntax ---> set_1.difference(set_2) or set_1 - set_2
eg
--
data_ = {1,2,3,4}
nums = {4,5,6}
print(nums.difference(data_))


symmetric_difference()
-----------------
-->different elements from the both
----->set_1,symmetric_difference(set_2)or set_1 ^ set_2
eg
---
data_ = {1,2,3,4}
nums = {3,4,5,6}
print(nums ^ data_)
print(data_.symmetric_difference(nums))


add()
-------
-->add() method will add only one element at a time
syntax --> set.add(element)

eg
---
data_ = {1,2,3,4}
print(data_)
data_.add(7)
print(data_)


update
---------
-->we can add more than one element by using update method
syntax-->set.update([elements]) or set_1.update(set_2)
eg
---
data_ = {1,2,3,4}
nums = {4,5,6}
print(data_)
data_.update([8,9])
print(data_)
data_.update(nums)
print(data_)

remove()
------
-->remove() method will del the given element from the set
---> if the element is not present in the set, it will raise error
syntax--->set.remove(element)
eg
data_ = {1,2,3,4}
data_.remove(3)
print(data_)
data_.remove(5)


discard
--------
--> the method is used to del the elements from the set , but never raise any error even the element not inside set
syntax-->set.discard(element)


clear()
-------
-->the method is used to del all elements from the set and it will written empty set
syntax-->set.clear()
eg
------
data_ = {1,2,3,4}
print(data_)
data_.clear()
print(data_)


dictionary
--------
-->dict is a collection of key : value pair
-->key must be unique and it should be immutable datatypes (int, str,tuple)
-->dict is represented in {}

details = {1:, 2
           'name': 'teja',
           {1,2]: [1,2]}


Accessing
--------
-->dict can access by calling key, we will get value from that key
syntax-->dict['key']

-->get method is also used to get the value from the that key
syntax-->dict.get(key)

eg
--
data_ = {'name':'Pravalli',
         'balance':7000,
         'Adr':1234567897654,
         'PANC':'GPXBP2898Y',
         2:[3,4]}


print(data_['Adr'])
print(data_.get(2))


UPDATE()
----------
-->Method is used update a key, incase if the key is not present inside dict then it add that key:value
syntax--> dict.update([key:value})

--> there is another way to update a key
syntax--> dict[key] = value
eg
---
data_ = {'name':'Pravalli',
         'balance':7000,
         'Adr':1234567897654,
         'PANC':'GPXBP2898Y',
         2:[3,4]}


print(data_)
data_['AC'] = 123456685458

dara_.update({'name':'sony'})
data_.update({'ATMPIN':7899})
print(data_)


values()
--------
-->values() method is used get all the values from the dict
syntax--> dict.values()
eg
---
data_ = {'name':'Pravalli',
         'balance':7000,
         'Adr':1234567897654,
         'PANC':'GPXBP2898Y',
         }


print(data_.values())

keys()
-----
-->keys method is used get all the key from the dict
syntax--> dict.keys()
eg
---
data_ = {'name':'Pravalli',
         'balance':7000,
         'Adr':1234567897654,
         'PANC':'GPXBP2898Y',
         }


print(data_.keys())

items()
-------
-->The method will get the key:value separated from the dict
syntax--> dict.items()
eg
------
data_ = {'name':'Pravalli',
         'balance':7000,
         'Adr':1234567897654,
         'PANC':'GPXBP2898Y',
         }


print(data_.items())

clear
-----
-->claer() method is used to del all data from dict
syntax --> dict.clear()
eg
-------
data_ = {'name':'Pravalli',
         'balance':7000,
         'Adr':1234567897654,
         'PANC':'GPXBP2898Y',
         }


print(data_)

del data_['Adr']
print(data_)
data_.clear()
print(data_)


if statement
-----------
--> if condition, become true, then it will exeecute inside block of code
--> incase it becomes false , then it will never enter into inside block

age = 15
if age>=18:
    print('Eligible to vote')
    
after execute

age = 19
if age>=18:
    print('Eligible to vote')


if else
-----------
-->else for if statement is a fall back statement, incase if condition is false then else block will execute


for statement
------------
--->for loop is used to iterate over a sequence or iterable datatypes



else in for
----------
--->unlike if-else, else block in for statement is executed after completed of all iterations

eg
---
nums = 'Python'
for num in nums:
    print(num)
else:
    print('for ended')

nums = [1,2,3,4,5,8,9]
for num in nums:
    print(num)
    if num == 3:
        break


val_ = [1,2,3,4,5,8,9]
for j in val_:
    if j % 2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')
    
    
break
--------
--> the break used to stop iteration based on the condition given
eg

nums = [1,2,3,4,5,8,9]
for num in nums:
    print(num)
    if num == 3:
        break

continue
--------
--> the continue is a key word used to skip current iteration based on the condition

nums = [1,2,3,4,5,8,9]
for num in nums:

    if num == 5:
        continue
    print(num)

pass
----------
-->A pass is called a space holder, that is used after statements like (if, for , else) not to raise any error

for j in range(1,11):
    if j == 15:
        print(j)
    else:
        pass

assert
-------
--> assert is a key word used to check the condition, incase the condition is false, it will raise the error(AssertionError)


age = 15
assert age >= 18, 'Not eligible to vote'
print('Your elligible to vote')


limit_ = int(input("Enter a number: "))
for i in range(2,limit_+1):
    count = 0
    for j in range(1,i+1):
        if i % j ==0:
            count +=1

    if count == 2:
        print(f'{i} is prime')

*
**
***
****
*****
star_ = int(input("Enter a number: "))
for i in range(1,star_+1):
    for j in range(1,i+1):
        print('*', end=" ")
    print()    
       
        
words_ = input("Enter a word: ")
vowels = 'aeiouAEIOU'
count = 0
for i in words_:
    if i in vowels:
        count +=1
        print(f'{i} is vowel')
print(count)




digits_ = [1,2,3,1,5,3]
empty_ = []
for i in digits_:
    if i not in empty_:
        empty_.append(i)
print(empty_)







digits_ = (1, 2, 3, 1, 5, 3)

for i in digits_:
    if digits_.count(i) > 1:
        print(i)

Arguments
--------
positional Arguments
-----------------
-->the arguments should be same at def line and calling incase if they are not same number will raise an error

def add_(a,b):
    print(a+b)
add_(a:5,b:7)    

default arguments
--------------
-->default arguments where the function will only consider the data at calling, even though data present at def line

eg
----

def feb_(num,num_2): 
    print(num + num_2)
feb_([1,3],[5,6])    


def prime(num=10,count = 1):
    for j in range(1,num+1):
        if num % j == 0:
            count += 1
            print(count)
    if count == 2:
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')
print(num = (input("Enter number: ")),count=0)     


keyword arguments
---------------
-->keyword arguments are sending arguments in a pair(a=2),and the pass order is not consider.........
eg
----
def data_(age,name,batch,location):
    print(name)
    print(age)
    print(batch)
    print(location)
data_(name='pravalli',age=22,location='vizag',batch=6)    

variable length argument
------------------
-->adding a (* call it as args ) before a variable at parameter we can pass tuple of arguments and can be access
with indexing

def all_(*Name):
    print(Name)
all_('Pravalli','Pothanapalli','Bujji','Advik','Honey')    

keyword length arguments
------------------------
eg
----
def Details(**data_):
    print(data_.keys())
Details(name='pravalli',age=22,location='vizag',batch=6)

return
--------
-->return keyword used inside the function, once the retuen is
executed means it will get back to calling with return values
eg
---
def al             0l_(a,b):
    return a-b
print(all_(7,9))


scope of variables
-----------------
1.local variable
------------
-->a variable is define inside the function call it as local variable where the variable can only access with in that function
eg
---
def display():
    name = 'pravalli'
    print(name)
display()
print()

2.global variable
---------------
--> a variable that is defined outside the function call and it can be access anywhere through out the program
eg
---
a = 90
def display():
    print(a)
display()
print(a)

a = 90
print(a)
def display():
    global a
    a = 10
display()
print(a)


global keyword
--------------
-->global is a keyword udes to reaccess new values to a variable that was already define outside thefunction call
eg
---
a = 90
print(a)
def display():
    global a
    a = 10
display()
print(a)

passing by value
------------
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(109)        


passing by reference
-----------------

num = 7
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(num)        

recursive function
----------------
--> the function call itself untill the base condition met....

lambda function
----------------
-->lambda function is small anonymous function
-->lambda can take n number arguments, but only with one expression.
-->the function is defined using lambda keyword

syntax-->lambda arguments : expression

eg
-----
add_ = lambda a,b,c, : a+b+c
print(add_(10,20,9))

even = lambda num : num % 2 == 0
print(even(7))

great_ = lambda a,b: a if a>b else b
print(great_(10,20))

cube_ = lambda a : a **3
print(cube_(5))


filter()
------------
-->filter()function will perform only on selected elements of iterables

syntax--> filter(lambda arguments: expression, iterable)

nums = [1,2,3,4,5]
data_ = filter(lambda a: a%2==0,nums)
print(list(data_))

nums = [1,2,3,4,5]
get_ = map(lambda a: a*5,nums)
print(list(get_))


map()
----------
-->map() function will perform on all elements of a iterable
sytnax-->map(lambda arguments: expression, iterable)

nums = [1,2,3,4,5]
get_ = map(lambda a:a%2==0,nums )
print(list(get_))

reduce()
----------
-->the reduce() function repeatedly applies a function to the elements and reduces them to one final alue.
--> it is available in the functools module.
syntax-->reduce(lambda arguments: expression, iterable)
eg
----
from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,range(1,10))
print(data_)

list comprehension
-----------------
-->list comprehension is the short form of syntax to create a list
 
syntax 1--> [expression loop condition]
syntax 2-->[expression condition else loop]
eg
---
old_ = (1,2,3,5,4)
new_ = [i for i in old_ if i%2==0 ]
print(new_)



nested comprehension
-------------------
-->using list comprehension generating list inside list


any_ = [[i*j for i in range(1,6)] for j in range(1,10)]
print(any_)

of = [[1,2,3,],
      [4,5,6,],
      [7,8,9,]]
      
data_ = [num
         for i in of for num in i ]
print(data_)

generator
---------------
-->a genarator is a special function which generate one value at a time

def all_():
    for j in range(1,10):
        yield j
j = all_()
print(next(j))
print(next(j))
print(next(j))
print(next(j))


modules
-----------
-->a module is a python file(.py) that written using function, variables, operators, etc.
eg
--
import math
print(math.pow(2,3))

1.bulit-in modules
-------------------
-->the modules are developed by programmers and those comes with installation
eg
----
1.sys
eg------

import sys
print(sys.path)
print(sys.version)


2.os
eg
---

import os
print(os.getcwd())

3.random
eg
--

import random
print(random.randint(1000,9999))

4.math
eg
----

import math
print(math.pow(2,3))
2.user-defined modules
----------------------
-->
importing specific function from 
syntax-->from module import function
eg
---
from pravalli import add_, sub_, pw_
print(add_(10,5))
print(sub_(10,5))
print(pw_(10,5))


using alias name
----------------
syntax-->import module as alias name
eg
----
import pravalli as nb
print(nb.add_(10,5))


Exception handling
==================
-->this is the way of handling errors
-->we can write any number exception for one code written at try block

-->try
=======
--> the try block where we can write a code which may contain errors..

syntax-->
try:
    code lines

-->except
==========
-->this will handle errors that are raised at try block..

syntax-->except ErrorName:
    print('ErrorName')

-->else
=========
-->the else block will only execute, if no error at tryblock

-->finally
==========
-->this block will execute regardless with the error at try block
eg
---
try:
    print(num)
    
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
else:
    print('No Error')
finally:
    print('end')


file handling
-------------
-->the file handler is a object, which is used to create,update, read, and delete...
modes
-------
r-->the (r) mode is used when the read() function is used
w
a
x
functions
===========
read()
write()



'''


with open('ATM PROJECT.txt','a') as file:
    file.write('This is teja, I am your python mentor')



































