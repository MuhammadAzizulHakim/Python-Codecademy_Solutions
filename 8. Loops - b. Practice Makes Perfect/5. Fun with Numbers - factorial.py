#version1:
import math

def factorial(x):
    return math.factorial(x)
    
print factorial(10)    
print factorial(3)
print factorial(1)
print factorial(0)


#version2:
def factorial(x):
    if x == 0: return 1
    else: return x * factorial(x - 1)
    
print factorial(10)    
print factorial(3)
print factorial(1)
print factorial(0)


#version3:
def factorial(x):
    num = 1
    for n in range(1, x + 1):
        num = num * n
    return num
        
print factorial(10)    
print factorial(3)
print factorial(1)
print factorial(0)


#version4:
def factorial(x):
    num = 1
    for n in range(x):
        num *= n + 1
    return num
        
print factorial(10)    
print factorial(3)
print factorial(1)
print factorial(0)


#version5:
def factorial(x):
    count = x
    total = 1
    while count != 0:
        total = total * count
        count -= 1
    return total
        
print factorial(10)    
print factorial(3)
print factorial(1)
print factorial(0)
