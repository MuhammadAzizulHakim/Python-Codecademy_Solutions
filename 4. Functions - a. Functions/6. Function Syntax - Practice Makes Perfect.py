def cube(number):
    return number ** 3

def by_three(number):
    if number % 3 == 0: 
        return cube(number)
    else: 
        return False

cube(9)
by_three(9)

print cube(9)
print by_three(9)
