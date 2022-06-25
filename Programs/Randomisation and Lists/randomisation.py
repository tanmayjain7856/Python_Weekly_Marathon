import random
import my_module

# randint(a,b)
random_number = random.randint(1, 10)
print(f'Random integer between 1 and 10: {random_number}')

# random()
random_float = random.random()
print(f'Random floating point number between 0 and 1: {random_float}')

# printing value in module file
print(my_module.pi)
