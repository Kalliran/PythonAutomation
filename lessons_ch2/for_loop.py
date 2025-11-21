# Some functions cans be called with multiple arguments separated by a comma, and range() is one of them.
# This lets you change the integer passed to range() to follow any sequence of integers, including starting at a number other than zero.

for i in range(12, 16):
    print(i) # Will print 12 and increment up to 16

# The range() function can also be called with three arguments. The first two arguments will be the start and stop values.
# The third will be the step-argument. The step is the amount that the variable is increased by after each iteration.

for i in range (0, 12, 2):
    print(i)

# You can use a negative number for the step-argument to make it count down.

for i in range(5, -1, -1):
    print(i)


for x in range(1, 4):
    print("We're on time %d" % (x)) # Replaces the %d with the value of x and prints the result