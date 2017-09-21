# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:14:20 2017

@author: Acer
"""

#Create string
word = "Hello World"
print(word)

# Accessing word using index
word[2]

# length of word
len(word)

# finding
#(i) count
word.count('o')
print("word.count(l):", word.count('l'))

Name= 'Holly'
Name.count('l')

#(ii)find
word.find('o')
Name.find('y')

#(iii)possition 
word.index('W')
Name.index('y')

# Replace

word.replace('Hello','hi')

# Slicing
word[0:]
word[1:4]

word[-3:]
word[1+1]
for i in word:
    print(i)
    
i=[0,1,3,5,7,9]
for x in i:
   print(word[x])

# Starts with Ends with
word.startswith('H')
word.startswith('W')

word.endswith('d')
word.endswith('l')

# Repeat string
word * 3
'Ayub'*2

# Replace
word.replace('Hello','Goodbye')

# Reverse string
' '.join(reversed(word))

'$'.join(reversed(Name))
'_'.join(reversed(word))

# Strip -> removing spaces
'       Ayub Quadri            '.strip()
'       Alice      '.rstrip()
'    Alice'.lstrip()

# concatination
a= "Ayub"
b = 'Quadri'

a + b 
(a, b)

#