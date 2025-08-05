import random
result = []
chance = 3
while chance >0: # ignore
    computer = random.randint(1,2) # int
    print(f'chance left {chance}')
    daru = input('Please enter your number between 1 to 2:') # string
    daru = int(daru) # changing data type string from string to integering
    if computer == daru:
        print('matched!!!')
        result.append("daru won!")
    else:
        print('not matched!')
        result.append("computer won")
    chance = chance - 1
print('game ends')
print(result)