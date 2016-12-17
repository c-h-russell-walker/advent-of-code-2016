import re
import sys

from collections import Counter

""" Checksum:
    - letters sorted by most common first
    - once we reach a tie we sort alphabetically until five chars is reached
"""

room_names = {}

with open(sys.path[0] + '/input.txt') as file:
    file_data = file.readlines()

lower_limit = ord('a')
upper_limit = ord('z')

for data in file_data:
    answer = []

    pre_checksum_chars = data.split('[')[0]
    sector_id = re.sub('[^0-9]+', '', pre_checksum_chars)
    checksum = re.sub('[^a-zA-Z]+', '', data.split('[')[1])

    chars = re.sub('[^a-zA-Z]+', '', pre_checksum_chars)
    ctr = Counter(chars)
    most_common = [c for c in ctr.most_common()]

    count_val = most_common[0][1] # default to highest count value

    sorted_list = [] # running tally of alphabetized sections
    alpha_list = [] # list to alphabetize (items with same count value)

    for ctr_item in most_common:
        if ctr_item[1] != count_val:
            count_val = ctr_item[1]
            sorted_list += alpha_list
            alpha_list = []
        alpha_list.append(str(ctr_item[0]))

        alpha_list.sort()

    sorted_list += alpha_list

    answer = ''.join(sorted_list)

    # Let's let the logic run its course and just truncate list when done
    answer = answer[:5]

    if answer == checksum:
        new_chars = []
        pre_sector_chars = re.sub('[^a-zA-Z-]+', '', pre_checksum_chars)
        for char in pre_sector_chars:
            if char != '-':
                val = ord(char.lower())
                val += (int(sector_id) % 26)
                if val > upper_limit:
                    diff = val - upper_limit
                    val = lower_limit + diff - 1

                new_chars.append(chr(val))
            else:
                new_chars.append(' ')

        room_names[sector_id] = ''.join(new_chars).rstrip()

for sector_id, name in room_names.items():
    if 'storage' in name and 'northpole' in name:
        print('The room `{name}` has the sectorId: {s_id}'.format(name=name, s_id=sector_id))
