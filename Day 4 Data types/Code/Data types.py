# intiger
a = 10
type(a)

# long int
b = 12344455l
type(b)

# Float
c = 1.34
type(c)

#complex
d = complex(2,5)
d
type(d)

# boolean
a = True
b = False
a
# a =1, b= 0 
c = a + b # c = 1 + 0
c
c = a - b # c = 1 - 0
c
c = a * b # c = 1 * 0
c
#c = a / b # c = 1/0 syntax error 
#c

# sets
a = set([12,'wwf',23.00])
a
type(a)
b = set([12,'wwf',23.00,12,'wwf',23.00,12,'wwf',23.00])
b  # even though it has repeated values it displays only unque set of items

# List
L = ['abc', 12, 78.90, complex(2,8), True]
L
type(L)
L[0] ='xyz' 
L

# tuple
T = ('abc', 23, complex(2,9), False)
T
T[1]

T[1] = 'xyz'

# Dictonary 
my_dict = {'name': 'John', 1: [2, 4, 3]}

my_dict = {'name': 'Alice', 'Age': 23, 'Education': 'BE(CS)', 'Addr':['Kukatpally', 'Hyd', 500081]}
my_dict
type(my_dict)

my_dict['name']
my_dict['Addr'][0]

# Mutable & immutables examples 
# tuple, str, frozen set
T = ('abc', 23, complex(2,9), False)
T[0]= 'xyz'
T
# strings
s= 'abc'
s= s+'d'
s[5]='d'

# frozen set
a = ('abc',122, 89.90, complex(2,5), True)
a = frozenset(a)

a[1]= 'xyz'

# Implicit Explicit Conversion
#implicit 
a= 4
a = 4 + True
a

# Explicit
a = int(89.90)
a

b = int(True)
b

c = float(89)
c


