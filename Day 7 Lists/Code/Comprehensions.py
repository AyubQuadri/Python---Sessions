# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 08:48:41 2017

@author: Acer
"""
# normal way of writing for loop to print odd numbers
for x in (range(10)):
	if x%2 != 0:
		print x
        
# using Comprehensions print odd numbers
odd = [i for i in range(10) if i%2 != 0]
odd

# Even numbers using for loop
for x in (range(11)):
	if x%2 == 0:
		print x
        
# using Comprehensions
even = [i for i in range(11) if i%2 == 0]
even
