animals = ['cat', 'alligator', 'mouse', 'shark', 'peacock', 'whale']

print 'You wish to have...'
for a in animals:
    if a == 'peacock':
        print 'A peacock is not a mammal!'
    print 'A', a
else:
    print 'A fine selections of animals!'

#example 2:

list_a = ['a', 'a', 'a', 'a', 'a', 'a', 'b', 'a']

for index,letters in enumerate(list_a):
    if letters == 'a':
        print "I am No.", index + 1, letters
else:
    print "Oops, I am spy b."
