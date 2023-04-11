import random

print('This is an interactive guessing game!',
    'You have to enter a number between 1 and 99 to find out the secret number.',
    "Type 'exit' to end the game.', 'Good luck!", sep='\n')

i = random.randint(1, 99)
inp = str(i)
j = 0

while inp != 'exit':
    print("What's your guess between 1 and 99?")
    inp = input()
    if inp == 'exit' or not inp.isdigit():
        print('Goodbye')
        continue
    j += 1
    if int(inp) > i:
        print('Too high!')
    elif int(inp) < i:
        print('Too low!')
    else:
        if i == 42:
            print('The answer to the ultimate question of life, the universe and everything is 42.')
        if j > 1:
            print("Congratulations, you've got it!")
            print('You won in', j, 'attempts!')
        else:
            print('Congratulations! You got it on your first try!')
        break