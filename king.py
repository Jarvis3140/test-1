def name():
    user_input = input('Enter your name: ')
    m = user_input.split()
    
    # Printing the first and last name with capitalization
    first_name = m[0].capitalize()
    last_name = m[-1].capitalize()

    a =  (first_name, last_name)
    # modified_name = (first_name.center(50), last_name.center(70))
    # print(modified_name)
    print(type(a))
import this 
name()


   