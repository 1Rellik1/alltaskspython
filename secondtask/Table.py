from array import *

table = "17-01-2003!0 None None 13%\n21-02-2000!1 None None 56%\n22-10-2000!0 None None 72%\n22-10-2000!0 None None 72%\n22-10-2000!0 None None 72% "
table = table.replace('None', '')
while table.find('%') != -1:
    if table[table.find('%') - 2] == '0':
        table = table.replace("100%", "1.0")
    else:
        n = (int(table[table.find('%') - 2]) * 10 + int(table[table.find('%') - 1])) / 100
        table = table.replace(table[table.find('%') - 2] + table[table.find('%') - 1] + '%', str(n))
while table.find('!') != -1:
    if table[table.find('!') + 1] == '0':
        table = table[:table.find('!') - 10] + "Не выполнено\n" + table[(table.find('!') - 10):]
        table = table[:table.find('!')] + table[(table.find('!') + 2):]
    else:
        table = table[:table.find('!') - 10] + "Выполнено\n" + table[(table.find('!') - 10):]
        table = table[:table.find('!')] + table[(table.find('!') + 2):]
while table.find('-') != -1:
    buff=table[table.find('-')+4:table.find('-')+8]+'/'+table[table.find('-')+1:table.find('-')+3]+'/'+table[table.find('-') - 2:table.find('-')]
    table=table[:table.find('-') - 2] + buff + table[(table.find('-') + 8):]
print(table)
