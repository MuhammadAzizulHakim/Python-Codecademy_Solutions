choice = raw_input('Enjoying the course? (y/n)')
if choice != 'y' and choice != 'n':
    while True:  # Fill in the condition (before the colon)
        choice = raw_input("Sorry, I didn't catch that. Enter again: ")
        if choice == 'y' or choice == 'n':
            break
