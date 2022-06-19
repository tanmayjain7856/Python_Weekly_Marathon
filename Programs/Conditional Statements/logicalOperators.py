a = 12

# and operator
print(a > 10 and a < 15)  # True when both conditions are true
print(a > 10 and a < 12)  # False when one condition is false
print(a < 5 and a < 9)  # False when both conditions are false

# or operator
print(a > 10 or a < 15)  # True when both conditions are true
print(a > 10 or a < 12)  # True when one condition is true
print(a < 5 or a < 9)  # False when both conditions are false

# not operator
# reverses the result so returns False even when 'and' condition is true
print(not(a > 10 and a < 15))
print(not(a < 5 or a < 9))  # True
