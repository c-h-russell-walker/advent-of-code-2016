import sys

from collections import Counter


result = []

with open(sys.path[0] + '/input.txt') as file:
    file_data = file.readlines()

list_cont = {}

for data in file_data:
    chars = data.rstrip()
    for i in range(0, len(chars)):
        if i not in list_cont:
            list_cont[i] = [chars[i]]
        else:
            list_cont[i].append(chars[i])

for vals in list_cont:
    ctr = Counter(list_cont[vals])
    result.append(ctr.most_common()[0][0])


print('Corrected message is: {}'.format(''.join(result)))
