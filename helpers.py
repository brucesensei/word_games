# helpers

def check_menu_input(number):
    '''Takes a number as input and continually asks the user for numeric input in the range
    until valid input received. returns int as str. '''
    choices = [str(i) for i in range(1,number+1)]
    while True:
        choice = input('Choose an option. ')
        if choice in choices:
            break
    return choice
