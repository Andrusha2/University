import csv


def file_reader(file_name):
    try:
        nums_list = []
        f = open(f'{file_name}')
        f.readline()
        reader = csv.reader(f)
        for row in reader:
            nums_list.append(int(*row))
        f.close()
    except FileNotFoundError:
        print(f'File {file_name} does not exist')
    except ValueError:
        print(f'File contains invalid data type')
    except IOError:
        print('IO error')
    except KeyboardInterrupt:
        print('The user interrupted the process')
    except Exception:
        print('Any other error')
    else:
        return nums_list
    return None

