import random



print('Welcome to the DiceRoll. To exit type exit. \n')

while True:
    roll = random.randint(1,6)
    print('Do you feel lucky? Guess the roll of the die: ')
    
    guess = input()
    if guess == 'exit':
        quit()
    elif int(guess) == roll:
        print(f'You got it! I rolled a {roll}.')
    else:
        print(f'You did not get lucky. I rolled a {roll}.')