row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]
print(f'{map[0]}\n{map[1]}\n{map[2]}')
position = input('Where do you want to put the treasure? \n')
horizontal = int(position[0])
vertical = int(position[1])
map[horizontal-1][vertical-1] = 'XX'
print(f'{map[0]}\n{map[1]}\n{map[2]}')
