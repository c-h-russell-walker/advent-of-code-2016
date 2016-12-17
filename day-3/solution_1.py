import sys

from triangle import Triangle

with open(sys.path[0] + '/input.txt') as file:
    file_data = file.readlines()

possible = 0

for data in file_data:
    sides = data.split()
    if len(sides) == 3:
        triangle = Triangle(sides)
        if triangle.valid_sides():
            possible += 1

print('Number of possible triangles: {}'.format(possible))
