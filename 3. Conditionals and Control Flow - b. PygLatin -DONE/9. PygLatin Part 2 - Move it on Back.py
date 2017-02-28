pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = original[0].lower()
    new_word = word + first + pyg
    print new_word
else:
    print 'empty'
