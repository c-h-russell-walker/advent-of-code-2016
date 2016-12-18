from hashlib import md5

# door_id = 'abc' # Test - result should be '05ace8e3'
door_id = 'ugkcyxxp'

idx = 0

password_vals = [None] * 8

while True:
    str_input = door_id + str(idx)
    idx += 1

    hash_val = md5(bytes(str_input, encoding='UTF-8')).hexdigest()

    if hash_val[:5] == '00000':
        try:
            pos = int(hash_val[5:6])
            assert (pos >= 0 and pos <= 7)
        except (ValueError, AssertionError):
            # Lines preceeding `continue` are purely informational
            valid_values = [value for value in password_vals if value is not None]
            print('Invalid values - pos: {} val: {}'.format(hash_val[6:7], hash_val[5:6]))
            print('Continuing - currently have {} values'.format(len(valid_values)))
            continue
        if password_vals[pos] is None:
            password_vals[pos] = hash_val[6:7]
        else:
            print('Skipping already filled position: {}'.format(pos))

        if all([p_val is not None for p_val in password_vals]):
            password = ''.join(password_vals)
            print('The decoded password is: {pwd}'.format(pwd=password))
            break
