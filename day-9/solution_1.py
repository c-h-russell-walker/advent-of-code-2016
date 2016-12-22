import sys

with open(sys.path[0] + '/input.txt') as file:
    file_data = file.readlines()

output = ''

assert len(file_data) == 1, 'Assumption is we only have one line for input'


chars = file_data[0].rstrip()
while True:
    # TODO - Oh god clean this up please - and make better names at least
    parts = chars.split('(', maxsplit=1)
    first = parts[0]
    if len(parts) > 1:
        # TODO - Make a recursive function maybe to handle multiple instructions
        instr = parts[1].split(')', maxsplit=1)[0]
        char_amt, repeat_amt = instr.split('x')
        to_repeat = parts[1].split(')', maxsplit=1)[1][:int(char_amt)]

        decom = first + (to_repeat * int(repeat_amt))
        chars = parts[1].split(')', maxsplit=1)[1][int(char_amt):]
    else:
        decom = chars
        output += decom
        break

    output += decom

# Test result should be 57:
# ADVENTABBBBBCXYZXYZXYZABCBCDEFEFG(1x3)AX(3x3)ABC(3x3)ABCY

print(output)
print('The decompressed length is: {}'.format(len(output)))