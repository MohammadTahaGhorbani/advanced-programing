import random

RANGE = 1000000
secret = random.randrange(1, RANGE + 1)

print('Guess a number between 1 and %d' % RANGE)

guess = 0

while guess != secret:
    guess = int(input('What is your guess? '))

    if guess < secret:
        print('Too low')
    elif guess > secret:
        print('Too high')
    else:
        print('You win!')