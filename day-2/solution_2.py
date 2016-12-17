import sys

# 5x5 keypad
#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D

keypad = [
    [None, None,  1, None,  None], # (0,0) (0,1) (0,2) (0,3) (0,4)
    [None,   2,   3,   4,   None], # (1,0) (1,1) (1,2) (1,3) (1,4)
    [  5,    6,   7,   8,     9 ], # (2,0) (2,1) (2,2) (2,3) (2,4)
    [None,  'A', 'B', 'C',  None], # (3,0) (3,1) (3,2) (3,3) (3,4)
    [None, None, 'D', None, None], # (4,0) (4,1) (4,2) (4,3) (4,4)
]

# start at five
position = [2, 0]
answer = []

with open(sys.path[0] + '/input.txt') as file:
    file_data = file.readlines()

for line in file_data:
    for instr in line.rstrip():
        if instr == 'D':
            try:
                if keypad[position[0] + 1][position[1]]:
                    position[0] += 1
            except IndexError:
                pass
        elif instr == 'U':
            if position[0] > 0 and keypad[position[0] - 1][position[1]]:
                position[0] -= 1
        elif instr == 'R':
            try:
                if keypad[position[0]][position[1] + 1]:
                    position[1] += 1
            except IndexError:
                pass
        elif instr == 'L':
            if position[1] > 0 and keypad[position[0]][position[1] - 1]:
                position[1] -= 1

    # make note of button to press
    key = keypad[position[0]][position[1]]
    print("Press the `{}` key".format(key))
    answer.append(str(key))

print("Press these keys: {}".format(', '.join(answer)))
