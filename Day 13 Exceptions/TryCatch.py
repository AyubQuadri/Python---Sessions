# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:45:59 2017

@author: ayubq
"""

a= 1
b= 0
try:
    c = a/b
except  ZeroDivisionError:
    print('Divide by zero error')
    
finally:
    print("good bye")
    
# file operations
a = input('Enter text to be inserted to the file: ')
print(a)

try:
    file = open("F:\\Sessions\\Python\\Day 13 Exceptions\File.txt", 'r')
    a = file.readline()
    print(a)
    b = file.readline()
    file.read(29)
    print(b)
    print(x)
    a = input('enter a value : ')
    a= int(a)
except IOError:
    print('unable to write to a file')
except EOFError:
    print('file has ended')
except NameError:
    print('varible not defined')
finally:
    print('closing the connection')
    file.close()
    
import numpy

try:
    import tensorflow as tf
    print('successfully imported the module')
    c = 1/1
    a = 5
    
except ImportError:
    print('unable to import pls install the module first')
except ZeroDivisionError:
    print('divide by zero')  
except EOFError:
    print('Name not entered')

finally:
    print('exit')
    
    
    
    
try:
    print(p)
except NameError:
    print('variable is not defined')
finally:
    print('closing')


def integer( prompt ):
    
    try:
        value_str = input( prompt )
        value_int = int( value_str )
    except ValueError:
        print ( "** Invalid input, assuming 0 **" )
        value_int = 0
    except EOFError:
        print("End of file error occurred.")
        return None

    return value_int

def main():
    try:
        numer = integer( "Enter the numerator: " )
        denom = integer( "Enter the denominator: " )
        print( numer, "divided by", denom, end=" " )
        result = numer/denom
        print( "yields", result )

    except ZeroDivisionError:
        print( "** Invalid: attempted to divide by zero **" )
    except EOFError:
        print("unsupported operand type (s) for /: 'int' and 'NoneType'")

    print( "Program halted" )

main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    