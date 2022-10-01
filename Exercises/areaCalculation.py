import math


def paint_cans_calc(height, width, coverage):
    area_of_wall = height * width
    can_coverage = area_of_wall / coverage
    no_of_cans = math.ceil(can_coverage)
    print(f'No. of paint cans required to paint the wall is: {no_of_cans}')


test_height = input('Enter height of wall: ')
test_width = input('Enter width of wall: ')
height = int(test_height)
width = int(test_width)
coverage = 5
paint_cans_calc(height=height, width=width, coverage=coverage)
