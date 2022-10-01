# Simple Function
def greet():
    print('Hello')
    print('How are you?')
    print('Bye')


greet()

# Function with Input


def greet_with_name(name):
    print(f'Hello {name}')
    print(f'How are you {name}?')
    print(f'Bye {name}')


greet_with_name('Aman')
greet_with_name('Sumit')
greet_with_name('Harsha')

# Function with multiple inputs


def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}?')


# Positional Arguments
greet_with('Aman', 'Delhi')

# Keyword Arguments
greet_with(location='Delhi', name='Aman')
