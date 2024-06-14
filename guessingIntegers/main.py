import random

name = input("What is you name?")
print(f'Hello, {name}!')

KEEP_GUESSING = True

x = random.randint(1,100)
numGuess = 1

while(KEEP_GUESSING == True):
    try:
        y = int(input('Guess an integer between 1 and 100!'))
    except ValueError:
        print('**************************************')
        print('An integer is a whole number, Silly!!!')
        print('              Try Again!              ')
        print('**************************************')
        continue
    if (x < y):
        print("TOO HIGH!")
        print("")
    if (x > y):
        print("TOO LOW!")
        print("")
    if (x == y):
        print('Good Guess! You Got It!!')
        print(f'It took you {numGuess} guesses!!')
        print("")
        KEEP_GUESSING = False
        break

    numGuess = (numGuess + 1)

print('#################')

print('# Rip and Tear! #')
print('#################')

