import sys

keypad = [
    [1, 2, 3], # (0,0) (0,1) (0,2)
    [4, 5, 6], # (1,0) (1,1) (1,2)
    [7, 8, 9], # (2,0) (2,1) (2,2)
]

# start at five
position = [1, 1]

answer = []

with open(sys.path[0] + '/input.txt') as file:
    file_data = file.readlines()

for line in file_data:
    for instr in line.rstrip():
        if instr == 'D':
            if position[0] < 2:
                position[0] += 1
        elif instr == 'U':
            if position[0] > 0:
                position[0] -= 1
        elif instr == 'R':
            if position[1] < 2:
                position[1] += 1
        elif instr == 'L':
            if position[1] > 0:
                position[1] -= 1

    # make note of button to press
    key = keypad[position[0]][position[1]]
    print("Press the `{}` key".format(key))
    answer.append(str(key))

print("Press these keys: {}".format(', '.join(answer)))
