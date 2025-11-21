# Created by: Michael Corleone
# Date: 11/4/2025
# Automate Boring Stuff With Python

"""
name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

"""
# Multiple ways to do the same thing

while True: #This would be an infinite loop because of 'True', but the if-statement with the 'break' condition ends it. 
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break

print('Thank you!')

while True:
    print('Who are you?')
    name = input()
    if name != 'Michael':
        continue # If the user enters any other name than 'Michael', the continue-statement keeps the loop going and it will continue to ask who you are.
    print('Hello Michael. What is the password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
