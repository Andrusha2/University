from dict_create import to_dict
from file_creator import file_create
from normal_form import to_normal
from translating import to_en

if __name__ == '__main__':
    final_dict = to_en(to_dict(to_normal(input('Enter the filename with chat: '))))
    file_create(final_dict, input('Enter the name of the new file: '))