# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:04:01 2017

@author: patel
"""
'''


 
# Write a Python program to calculate the length of a string.
z='xyzab cdef '
print(len(z))



#  Write a Python program to remove the characters which have odd index values of a given string.
string='abcdefghijkl'
final=''
for i in range(len(string)):
    if i % 2 == 1:
        final = final + string[i]
print(final)


# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
 #Sample String : 'abc', 'xyz'Expected Result : 'xyc abz‘
 
a="abc"                #xyc abz
b="xyz"
print(b[0:2] + a[2:] + " " +a[0:2] + b[2:])


# Write a Python program to check whether a string starts with specified characters.
t="Good"
print(t.startswith("g"))
print(t.endswith("o"))
print(t.capitalize())


 
