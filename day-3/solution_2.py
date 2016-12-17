import sys

from triangle import Triangle

with open(sys.path[0] + '/input.txt') as file:
    file_data = file.readlines()

possible = 0
rows = []
cols = []

for data in file_data:
    rows.append(data.split())
    if len(rows) == 3:
        for i in range(0, 3):
            cols.append([rows[0][i], rows[1][i], rows[2][i]])
        rows = []

for sides in cols:
    if len(sides) == 3:
        triangle = Triangle(sides)
        if triangle.valid_sides():
            possible += 1

print('Number of possible triangles: {}'.format(possible))
