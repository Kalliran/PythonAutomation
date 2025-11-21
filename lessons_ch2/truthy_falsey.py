# Created by: Michael Corleone
# Date: 11/4/2025
# Automate Boring Stuff With Python

# If the user enters a blank string for name, then the while-statement's condition will be True, and the program continues to ask for a name.
# If the value for numOfGuests is not 0, then the condition is considered to be True, and the program will print a reminder for the user.
# You could have entered: not name != ''  instead of: not name  , and numOfGuests != 0 instead of numOfGuests, but using the truthy and falsey values can make your code easier to read.

name = ''

while not name: # if name is false, then the statement is True (while (name != true))
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')