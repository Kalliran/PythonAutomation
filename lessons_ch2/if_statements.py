number = 20
number = number + 1

print(number)

# What would be the value of the following two expressions:
print('spam' + 'spamspam')
print('spam' * 3)

# What three functions can be used to get the integer, floating-point number, or string version of a value?
int()
str()
float()

print('I have eaten ' + str(99) + ' burritos.')

# The round() method will automatically round upwards if the 2nd parameter is omitted.
score = 3.149278
print(round(score, 2))

# Control flow:
if (score == 3.149278):
    print(score)
else:
    print('Error')

name = ''
# name = 'michael'
print('What is your name?')
input(name)

if (name == 'alice'):
    print('Hello ' + str(name))

age = int(input('Please enter your age: '))

if name == 'alice':
    print('Hi, Alice')
elif age == 12:
    print("Okay, you're Alice.")
elif age < 12:
    print('You are not Alice, kiddo.')
elif age < 20 and age > 12:
    print('You are possibly Alice.')
elif age > 200:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 70:
    print('You are not Alice, granny.')
else:
    print('Access Denied: You are not Alice.')

    
spam = int(input())

if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
        print('spam') # This gets printed instead of ham because it's the most recent in the stack
print('spam')