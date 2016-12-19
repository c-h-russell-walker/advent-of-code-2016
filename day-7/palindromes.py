def check_for_palindromes(strings=[]):
    for word in strings:
        if check_for_palindrome(word):
            return True
    return False

def check_for_palindrome(word):
    """
        For sake of puzzle we consider consecutive letters not a palindrome
        e.g. `aaaa`
        Also we assume palindrome of four characters
    """

    for i in range(1, len(word)):
        # Positive example: `abba`
        # Negative example: `aaaa`
        try:
            # if next equals current
            if word[i] == word[i+1]:
                # check if previous equals two places from current and all four aren't same
                if word[i-1] == word[i+2] and word[i-1] != word[i]:
                    return True
        except IndexError:
            return False
    return False