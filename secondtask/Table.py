from array import *
import re

table = "17-01-2003!0 None None 13%\n21-02-2000!1 None None 56%\n22-10-2000!0 None None 72%\n22-10-2000!0 None None " \
        "72%\n22-10-2000!0 None None 72%"
print(table)
result = re.findall(r'[\n]', table)
i = 0
while i < len(result):
    if i != 0:
        one = table[27 * i:26 + (26 * (i)) + i]
        two = table[27 * (i + 1):26 + (27 * (i + 1))]
        if one == two:
            table = table[:27 * i] + table[27 * (i + 1):]
            i -= 1
            result = re.findall(r'[\n]', table)
        i += 1
    else:
        one = table[27 * i:26]
        two = table[27 * (i + 1):27 + (26 * (i + 1)):]
        if one == two:
            table = table[:27 * i] + table[27 + (26 * (i + 1)):]
            result = re.findall(r'[\n]', table)
            i -= 1
        i += 1
table = table.replace('None ', '')
table = table.replace('\n', '')
while table.find('!') != -1:
    result = re.search(r'[0-9]', table)
    if table[table.find('!') + 1] == '0':
        table = table[:result.start()] + "Не выполнено         " + table[result.start():]
        table = table[:table.find('!')] + table[(table.find('!') + 2):]
    else:
        table = table[:result.start()] + "Выполнено          " + table[result.start():]
        table = table[:table.find('!')] + table[(table.find('!') + 2):]
result = re.search(r'[0-9]', table)
table = table[:result.start()] + "\n" + table[result.start():]
while table.find('-') != -1:
    buff = table[table.find('-') + 4:table.find('-') + 8] + '/' + table[table.find('-') + 1:table.find(
        '-') + 3] + '/' + table[table.find('-') - 2:table.find('-')] + "          "
    table = table[:table.find('-') - 2] + buff + '' + table[(table.find('-') + 8):]
while table.rfind('%') != -1:
    if table[table.find('%') - 2] == '0':
        table = table.replace("100%", "1.0")
    else:
        n = (int(table[table.find('%') - 2]) * 10 + int(table[table.find('%') - 1])) / 100
        table = table + str(n) + "                 "
        table = table[:table.find('%') - 2] + table[table.find('%') + 1:]
table = table[:table.rfind('/') + 3] + "\n" + table[table.rfind('/') + 12:]
print(table)
27
