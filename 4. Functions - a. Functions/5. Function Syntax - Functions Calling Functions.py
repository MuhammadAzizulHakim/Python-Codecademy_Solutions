def one_good_turn(n):
    return n + 1
    
def deserves_another(n):
    return one_good_turn(n) + 2

one_good_turn(0)
deserves_another(0)

print one_good_turn(0)
print deserves_another(0)
