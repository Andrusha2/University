def file_create(final_dict, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in final_dict:
            f.write('|'.join(map(str, i)) + '\n')
