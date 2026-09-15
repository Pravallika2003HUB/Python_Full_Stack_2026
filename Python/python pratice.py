'''
input formatting : accept input frpm user
integer,float,string,comma separated values,space separated values

#input from user ---> input()

name = input("enter the name:")
print(name)
print(type(name))
print(len(name))

#split()
#by default it will be space separated
name = input("enter the name:").split(',')
print(name)
print(type(name))
print(len(name))

#accept single integer,multiple integer values,group of integers

num1 = int(input("enter the number:"))
print(num1)
print(type(num1))


#every built-in datatype is a built-in function--> functions --> object

#usage of map()-->group of integers
numbers = list(map(int,input("enter the values:").split(',')))
print(numbers)
print(type(numbers))

#group of float values
temperatures = list(map(float,input("enter the values:").split(',')))
print(temperatures)
print(type(temperatures))
'''
#accept multiple values--> integers,float,names(str)...
temp,pressure = map(float,input("enter the values:").split(','))
print("temp is",temp)
print("pressure is",pressure)
