import random

names_string = input('Give me everybody\'s name, separated by comma. \n')
names = names_string.split(', ')

# First way of selecting random name
random_number = random.randint(0, len(names)-1)
print(f'{names[random_number]} is going to buy the meal today!')

# Second way of selecting random name
print(random.choice(names) + ' is going to buy the meal today!')
