import urllib.request
import re
import csv

pattern = r'(?:-link">)(?P<title>[^<]+)(?:(?:.+(?:[^"]+)){1}"org-widget-header__meta">[^"]+|(?:.+(?:[^"]+)))(?:.+(?:\s+))(?P<address>.+)(?:\D+)(?P<phone>[^<]+)(?:(?:.+)(?:[^>]+)){4}>(?P<time>[^<]+)'
f = open("res.csv", 'w', encoding='utf-8')
writer = csv.writer(f, delimiter=';', lineterminator='\r')
writer.writerow(('title', 'address', 'phone', 'time'))
for i in range(1, 6):
    url = f'https://msk.spravker.ru/avtoservisy-avtotehcentry/?page={i}'
    res = re.findall(pattern, urllib.request.urlopen(url).read().decode())
    print(res)
    for j in res:
        writer.writerow(j)


