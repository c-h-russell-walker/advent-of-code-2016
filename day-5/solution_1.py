from hashlib import md5

# door_id = 'abc' # Test
door_id = 'ugkcyxxp'

idx = 0

password_vals = []

while len(password_vals) < 8:
    str_input = door_id + str(idx)
    idx += 1

    m = md5(bytes(str_input, encoding='UTF-8'))
    hash_val = m.hexdigest()

    if hash_val[:5] == '00000':
        password_vals.append(hash_val[5:6])

print(''.join(password_vals))
