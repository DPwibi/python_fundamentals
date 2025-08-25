import random
from funs import rock_paper_scissors

options = ('rock', 'paper', 'scissors')
computer = random.choice(options)

user = input('write your option: ')
result = rock_paper_scissors(computer,user)

print(f'{result} won')
