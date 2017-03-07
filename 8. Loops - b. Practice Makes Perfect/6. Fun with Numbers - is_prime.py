def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2,x):
        if x % n == 0:
            print n
            return False
    else:
        return True


print is_prime(1)
print is_prime(2)
print is_prime(3)
print is_prime(4)
print is_prime(5)
