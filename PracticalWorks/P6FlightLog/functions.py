import re

with open('logs.txt', encoding='utf-8') as f:
    logs = f.read()
pattern = r"\d+ (?:прибыл из|отправился в) [А-я]+ в \d{2}:\d{2}:\d{2}"
matches = re.findall(pattern, logs)
result = list()
for i in matches:
    if 'из' in i:
        result.append(f'[{i[-8:]}] - Поезд №{i[:3]} {i[11:-11]}')
    else:
        result.append(f'[{i[-8:]}] - Поезд №{i[:3]} {i[15:-11]}')

with open(input('Введите название файла: '), 'w', encoding='utf-8') as f:
    for i in result:
        f.write(i + '\n')