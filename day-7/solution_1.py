import re
import sys

from palindromes import check_for_palindromes, check_for_palindrome

"""
    Assumptions:
    all IP addresses are only lowercase alpha characters
"""

ips = []

with open(sys.path[0] + '/input.txt') as file:
    file_data = file.readlines()

for data in file_data:
    chars = data.rstrip()

    # Left-most string (not in brackets)
    pre_brk = chars.split('[')[0]

    # Strings not in brackets but between bracketed strings
    betweens = re.findall('\](.*?)\[', data, re.DOTALL)

    post_br_idx = data.rfind(']')
    assert post_br_idx > 0
    # Right-most string (not in brackets)
    post_br = chars[post_br_idx+1:]

    # What's in-between brackets
    brackets = re.findall('\[(.*?)\]', data, re.DOTALL)

    # If palindrome in-between brackets we can skip
    if check_for_palindromes(brackets):
        continue

    if check_for_palindromes(betweens) or \
        check_for_palindrome(pre_brk) or \
        check_for_palindrome(post_br):
        ips.append(data)


# print('Valid IPs are: \n{}\n'.format(''.join(ips)))

# Length of valid IPs is `2` for test input
print('Number of valid IPs is: {}'.format(len(ips)))
