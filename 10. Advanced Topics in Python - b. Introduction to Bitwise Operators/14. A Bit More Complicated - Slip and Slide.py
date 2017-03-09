#version1:
def flip_bit(number,n):
    mask = 0b1 << n-1
    result = number ^ mask
    return bin(result)
    
 
#version2:
def flip_bit(number,n):
    return bin(number ^ 2**(n-1))
