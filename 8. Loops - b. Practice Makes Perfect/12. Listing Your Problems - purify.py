def purify(numbers):
    return [x for x in numbers if x % 2 == 0]
    
print purify([1,2,3,4,5,6,7,8,9,0])
