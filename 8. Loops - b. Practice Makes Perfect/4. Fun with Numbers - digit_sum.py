#version 1:

digits = []
def digit_string(n):
    for digit in str(n):
        digits.append(digit)
    print "Separated digits: %s " % digits
    return digits
    
def digit_sum(digits):
    result = 0
    for digit in digits:
        result += int(digit)
    print "Sum of digits in the number %s is %s." % (n, result)
    return result
    
n = int(raw_input("Tell me your number Sire: "))
digit_string(n)
digit_sum(digits)


#version 2:

def digit_sum(n):
    n = abs(n)
    total = 0
    while n >= 1:
        total += (n % 10)
        n = n//10
    return total
print digit_sum(1234)


#version 3:

def digit_sum(n = 0):
    return sum([int(i) for i in str(n)])
    
print digit_sum(1234)
