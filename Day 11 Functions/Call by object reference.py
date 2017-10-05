# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 23:54:42 2017

@author: ayubq
"""


# pass by value
a = 10
def changeIt(value):
    print('passed value:', value)
    print('location of value:',id(value))
    value = 20
    print('changed value:', value)
    print('location value after update:',id(value))
    return value

print('location of a', id(a))
changeIt(a)
a= print('Check the value of a:',a)
print('location value a after update:',id(a))

# Pass by reference 

b= [1,2,3]

def change(value):
    print('passed value', value)
    print('location:',id(b))
    b.append(90)
    b[0]= 10
    print('changed value', b)
    print('location:',id(b))
    return b 

change(b)
print('reteurned balues ',b )
print('location:',id(b))

# Call by reference object 
def double_it(value):
    print(value, id(value))
    value = value * 2
    print(value, id(value))
    return value

a = 3
print(a, id(a))
doubled_value = double_it(a)
print(doubled_value,id(doubled_value))
