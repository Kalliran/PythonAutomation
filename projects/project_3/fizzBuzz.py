


for x in range(1, 101):

    if (x % 3 == 0 and x % 5 == 0):
        print('%d FizzBuzz' % (x))
    if (x % 3 == 0):
        print('%d Fizz' % (x))
    elif (x % 5 == 0):
        print('%d Buzz' % (x))
    else:
        print('%d This number is not divisible by 3 or 5' % (x))