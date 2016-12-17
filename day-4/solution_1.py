import re
import sys

from collections import Counter

""" Checksum:
    - letters sorted by most common first
    - once we reach a tie we sort alphabetically until five chars is reached
"""

# Goal is to get total sum of numeric sector IDs of real room
result = 0

with open(sys.path[0] + '/input.txt') as file:
    file_data = file.readlines()

for data in file_data:
    answer = []

    pre_sector_chars = data.split('[')[0]
    sector_id = re.sub('[^0-9]+', '', pre_sector_chars)
    checksum = re.sub('[^a-zA-Z]+', '', data.split('[')[1])

    chars = re.sub('[^a-zA-Z]+', '', pre_sector_chars)
    ctr = Counter(chars)
    most_common = [c for c in ctr.most_common()]

    count_val = most_common[0][1] # default to highest count value

    sorted_list = [] # running tally of alphabetized sections
    alpha_list = [] # list to alphabetize (items with same count value)

    # TODO - Add comments to clarify
    for ctr_item in most_common:
        if ctr_item[1] != count_val:
            count_val = ctr_item[1]
            sorted_list += alpha_list
            alpha_list = []
        alpha_list.append(str(ctr_item[0]))

        alpha_list.sort()

    sorted_list += alpha_list

    answer = ''.join(sorted_list)

    # Let's let the logic run it's course and just truncate list when done
    answer = answer[:5]

    if answer == checksum:
        result += int(sector_id)


print('Totalled sector IDs is: {}'.format(result))
