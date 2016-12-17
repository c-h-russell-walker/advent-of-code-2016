import sys

with open(sys.path[0] + '/input.txt') as file:
    file_data = file.read()

x = y = 0
direction = 0  # Let's use 0, 1, 2, 3 = N, E, S, W respectively

instructions = file_data.split(', ')

# instructions = ['R2', 'L3']
# instructions = ['R2', 'R2', 'R2']
# instructions = ['R5', 'L5', 'R5', 'R3']

for instr in instructions:

    if instr[0] == 'R':
        direction += 1
    else:
        direction -= 1
    direction = direction % 4

    blocks = int(instr[1:])

    # NORTH
    if direction == 0:
        y += blocks
    # EAST
    elif direction == 1:
        x += blocks
    # SOUTH
    elif direction == 2:
        y -= blocks
    # WEST
    elif direction == 3:
        x -= blocks

print('X blocks away: {x}'.format(x=x))
print('Y blocks away: {y}'.format(y=y))
print('Total blocks away: {total}'.format(total=abs(y) + abs(x)))
