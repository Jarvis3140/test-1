def name():
    user_input = input('Enter your name: ')
    m = user_input.split()
    
    # Printing the first and last name with capitalization
    first_name = m[0].capitalize()
    last_name = m[-1].capitalize()

    print(first_name, last_name)

name()
