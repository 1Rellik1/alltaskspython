from array import *
import re

table = "17-01-2003!0 None None 13%\n21-02-2000!1 None None 56%\n22-10-2000!0 None None 72%\n22-10-2000!0 None None " \
        "72%\n22-10-2000!0 None None 72% "
print(table)
table = table.replace('None ', '')
table = table.replace('\n', '')
while table.find('!') != -1:
    result = re.search(r'[0-9]', table)
    if table[table.find('!') + 1] == '0':
        table = table[:result.start()]+"Не выполнено " + table[result.start():]
        table = table[:table.find('!')] + table[(table.find('!') + 2):]
    else:
        table =table[:result.start()]+ "Выполнено " + table[result.start():]
        table = table[:table.find('!')] + table[(table.find('!') + 2):]
result = re.search(r'[0-9]', table)
table = table[:result.start()]+"\n" + table[result.start():]
while table.find('-') != -1:
    buff = table[table.find('-') + 4:table.find('-') + 8] + '/' + table[table.find('-') + 1:table.find(
        '-') + 3] + '/' + table[table.find('-') - 2:table.find('-')]
    table = table[:table.find('-') - 2] + buff + '' + table[(table.find('-') + 8):]
print(table)
while table.rfind('%') != -1:
    result = re.search(r'$', table)
    print(result.end())
    if table[table.find('%') - 2] == '0':
        table = table.replace("100%", "1.0")
    else:
        n = (int(table[table.find('%') - 2]) * 10 + int(table[table.find('%') - 1])) / 100
        table = table[:result.end()+2] + str(n) + table[(table.rfind('%'))+1:]
# result = re.search(r'[.]', table)
# table = table[:result.start()-2]+ "\n" + table[result.start()-2:]
print(table)
