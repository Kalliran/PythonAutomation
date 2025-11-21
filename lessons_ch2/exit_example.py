import sys

while True:
    print('Type exit to exit.')
    response = input() # creating a variable to store the user's input
    if response == 'exit': # checking if the user types what we want, if not, display what they type with the print function
        sys.exit()
    print('You typed ' + response + '.')