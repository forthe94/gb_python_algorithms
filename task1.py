import hashlib as hl

def calc_substring_count_hash(inp_string):
    str_len = len(inp_string)

    hashes_list = []
    for ent in range(1, str_len + 1):
        for sub_str in range(str_len - ent + 1):
            str_hash = hl.sha1(inp_string[sub_str:ent + sub_str].encode('utf-8')).hexdigest()
            if str_hash not in hashes_list:
                hashes_list.append(str_hash)
    return len(hashes_list)

inp = input('Введите строку: ')

print(f'Количество подстрок: {calc_substring_count_hash(inp)}')
