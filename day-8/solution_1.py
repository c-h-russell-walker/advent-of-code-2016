import sys

from grid import Grid

"""
    Big TODO - think about leveraging matrix math
    For now, going to use brute fruce approach to assign/move pixels
"""

# 6 pixels tall
# 50 pixels wide
keypad = Grid(height=6, width=50)

# Test keypad - 3 tall and 7 wide
# keypad = Grid(height=3, width=7)

with open(sys.path[0] + '/input.txt') as file:
    file_data = file.readlines()

for data in file_data:
    instr = data.rstrip().split(' ')

    if instr[0] == 'rect':
        x, y = instr[1].split('x')
        for y_coord in range(int(y)):
            for x_coord in range(int(x)):
                keypad.set_true(x_coord, y_coord)
    elif instr[0] == 'rotate':
        amt = int(instr[4])
        row_col = int(instr[2].split('=')[1])
        if instr[1] == 'row':
            keypad.shift_row(y=row_col, amt=amt)
        elif instr[1] == 'column':
            keypad.shift_col(x=row_col, amt=amt)
    else:
        raise Exception('Invalid function name found')

print(keypad)
print('The amount of lit pixels is: {}'.format(keypad.count_true()))
