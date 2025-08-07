import random
# make a random number between 1 to 100

computer = random.randint(1,100)
chances = 10

while chances > 0:
    user = int (input(f'{chances} left Please enter your number'))
    if user > computer:
        print("Your number is too big")
    elif user < computer:
        print("Your number is too small")
    else:
        print('you guessed it!')
        break
    
    chances = chances - 1
