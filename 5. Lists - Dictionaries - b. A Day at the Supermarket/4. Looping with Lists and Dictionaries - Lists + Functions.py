def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

lost = [4, 8, 15, 16, 23, 42]
small = count_small(lost)
print small

# Write your function below!
def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count += 1
    return count

print fizz_count(["fizz", "fuzz", "fizz", "fazz", "fizz", "fozz"])
