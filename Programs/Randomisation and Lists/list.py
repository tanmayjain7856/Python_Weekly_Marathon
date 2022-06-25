# Lists
colors = ['blue', 'crimson', 'green', 'indigo', 'orange',
          'purple', 'red', 'violet', 'white', 'yellow']

# To print whole list
print(colors)

# To print a particular data in list
print(colors[2])
print(colors[-1])

# To change an item in list
colors[2] = 'grey'
print(colors[2])

# To add an item to list
colors.append('zucchini')
print(colors)

# To add multiples items to list
colors.extend(['brown', 'olive', 'maroon', 'magenta', 'cream'])
print(colors)

# Nested List
fruits = ['Strawberries', 'Apples', 'Grapes', 'Peaches', 'Pears']
vegetables = ['Spinach', 'Tomatoes', 'Celery', 'Potatoes']
nested_list = [fruits, vegetables]
print(nested_list)
