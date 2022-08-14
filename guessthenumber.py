import random

n = int(input('Select the highest number i should think of:'))
secretNum = random.randint(1,n)

print(f'I am thinking of a number from 1 till {n}. What is it? ')
guess = int(input())

while guess not secretNum:
    print(f'Your guess was wrong by {Abs(guess-secretNum)}.'

print('You got it! It was ', secretNum)


#syntax errors come up on this
#investigate and deal with later
#also needs cleanup with functions needing creation and all that good stuff