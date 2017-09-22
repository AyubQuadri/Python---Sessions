# read the values form users



print('Enter the number:')

num1=int(input())

print('enter another number:')

num2=int(input())
num3=num1+num2

print(num3)
num4=num1-num2 
print(num4)

num5=num1 & num2
print(num5)
num6=num1 | num2
print(num6)
num7=num1 ^ num2
print(num7)
print(num1>>1)

if(num1==num2):
    print("Both are same")
else:
    print("Not same")

if(num1>=10):
    print("num1 is >=")
else:
    print("num1 is !>=")