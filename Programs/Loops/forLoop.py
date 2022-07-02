fruits = ['Apple', 'Banana', 'Orange', 'Peach']
for fruit in fruits:
    print(fruit)
    print(fruit + ' Pie')

# Range function without step
for number in range(1, 10):
    print(number)

# Range function with step
for number in range(1, 10, 2):
    print(number)

# adding numbers from 1 to 100
sum = 0
for number in range(1, 101):
    sum += number
print(sum)
