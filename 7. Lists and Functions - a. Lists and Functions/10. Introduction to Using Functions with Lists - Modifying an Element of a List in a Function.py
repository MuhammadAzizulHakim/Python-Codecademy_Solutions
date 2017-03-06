def list_function(n):
    n[1] += 3
    return n

n = [3, 5, 7]
print list_function(n)

#version 2:

def list_function(n):
    n[1] = n[1] + 3
    return n

n = [3, 5, 7]
print list_function(n)
