# Type Error

# len(31435445)
# type error in above lines because len() doesn't accept integer

# lenChar = len(input('What is your name?'))
# print('Your name has ' + lenChar + ' characters.')
# type error in above lines due to string and integer conctenation

# Type Checking
lenChar = len(input('What is your name?'))
print(type(lenChar))

# Type Conversion/Casting
lenChar = len(input('What is your name?'))
newLenchar = str(lenChar)
print('Your name has ' + newLenchar + ' characters.')
