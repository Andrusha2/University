
def read_file(file_name):
    with open(f'{file_name}', 'r') as file:
        return set(map(lambda x: x.lower(), file.read().split()))


def save_file(new_file_name, file):
    with open(f'{new_file_name}', 'w') as new_file:
        new_file.write('\n'.join(sorted(file)))
