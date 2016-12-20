import re
import sys


"""
    Assumptions:
    all IP addresses are only lowercase alpha characters

    TO NOTE: These palindrome functions have been modified from the
    originals in palindromes.py - TODO added about consolidating
"""

def check_for_palindromes(strings=[]):
    palins = []
    for word in strings:
        if check_for_palindrome(word):
            palins += check_for_palindrome(word)
    return palins

# TODO - Move these functions into the `palindromes` file
def check_for_palindrome(word):
    """
        For sake of puzzle we consider consecutive letters not a palindrome
        e.g. `aaa`
        Also we assume palindrome of **three** characters
        :return: found three char palindrome or False
    """
    palins = []

    for i in range(1, len(word)):
        # Positive example: `xyx`
        # Negative example: `xxx`
        try:
            # if previous equals next and current isn't same
            if word[i-1] == word[i+1] and word[i] != word[i-1]:
                # Only append three letter word
                palins.append(word[i-1:i+2])
        except IndexError:
            return palins
    return palins


supported_count = 0

# with open(sys.path[0] + '/test_input_2.txt') as file:
with open(sys.path[0] + '/input.txt') as file:
    file_data = file.readlines()

for data in file_data:
    # Will be lists of all palindromes
    outside_ip_palins = []
    inside_ip_palins = []
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

    inside_ip_palins = check_for_palindromes(brackets)

    outside_ip_palins = check_for_palindromes(betweens)
    outside_ip_palins += check_for_palindrome(pre_brk)
    outside_ip_palins += check_for_palindrome(post_br)

    # Compare palindromes from inside and outside IPs
    unsupported = [
        not len(inside_ip_palins),
        not len(outside_ip_palins),
    ]
    # No palindromes in either
    if any(unsupported):
        continue

    for palin in outside_ip_palins:
        if not len(palin):
            continue
        # Do swapping
        word = list(palin)
        word[0], word[1], word[2] = word[1], word[0], word[1]
        # Check if swapped version inside brackets
        if ''.join(word) in inside_ip_palins:
            supported_count += 1
            # As long as we've found one we can increment, break & move on to next one
            break


# Length of valid IPs is `3` for test input
print('Number of IPs supporting SSL is: {}'.format(supported_count))
