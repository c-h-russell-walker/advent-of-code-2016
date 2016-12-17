import sys


with open(sys.path[0] + '/input.txt') as file:
    file_data = file.read()

x = y = 0
direction = 0  # Let's use 0, 1, 2, 3 = N, E, S, W respectively

instructions = file_data.split(', ')

# Test Data
# instructions = ['R8', 'R4', 'R4', 'R8']

visits = set()

return_visit = None

def log_visit(x, y):
    key = '{x}{y}'.format(x=x, y=y)
    if key in visits:
        return (x, y)
    else:
        visits.add(key)
        return None

for instr in instructions:

    if instr[0] == 'R':
        direction += 1
    else:
        direction -= 1
    direction = direction % 4

    blocks = int(instr[1:])

    # NORTH
    if direction == 0:
        for i in range(y, y+blocks):
            return_visit = log_visit(x, i)
            if return_visit is not None:
                break
        y += blocks
    # EAST
    elif direction == 1:
        for i in range(x, x+blocks):
            return_visit = log_visit(i, y)
            if return_visit is not None:
                break
        x += blocks
    # SOUTH
    elif direction == 2:
        for i in range(y, y-blocks, -1):
            return_visit = log_visit(x, i)
            if return_visit is not None:
                break
        y -= blocks
    # WEST
    elif direction == 3:
        for i in range(x, x-blocks, -1):
            return_visit = log_visit(i, y)
            if return_visit is not None:
                break
        x -= blocks

    if return_visit is not None:
        break

if return_visit is not None:
    ret_x, ret_y = return_visit
    print('First return visit coords: {x}, {y}'.format(x=ret_x, y=ret_y))
    print('Total blocks away: {total}'.format(total=abs(ret_x) + abs(ret_y)))
else:
    print('Huh, all unique visits?')