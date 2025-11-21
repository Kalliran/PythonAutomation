import random, sys, os, math

for i in range(5):
    print(random.randint(1, 10))


# This code snippet required the module: import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')