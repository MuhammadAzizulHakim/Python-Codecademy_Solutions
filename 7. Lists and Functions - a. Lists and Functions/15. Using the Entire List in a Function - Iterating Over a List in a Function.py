n = [3, 5, 7]

def total(numbers):
    result = 0
    for number in numbers:
        result += sum(numbers)
        return result
