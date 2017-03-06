#version 1:

def is_int(x):
    if round(x) - x == 0:
        return True
    else:
        return False
        
#version 2:

import math

def is_int(x):
    check = str(x)
    if '.' in check:
        is_int = math.floor(x)
    if x - is_int > 0:
        print 'False'
        return False
    elif x - is_int == 0:
        print 'True'
        return True
    elif '.' not in check:
        print 'True'
        return True

is_int(3.01)
