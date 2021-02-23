import re

def f21(mas):
    if mas[1] == 2004:
        if mas[0] == 'kit':
            return 10
        elif mas[0] == 'abnf':
            if mas[3] == 'red':
                return 6
            elif mas[3] == 'flux':
                return 9
            elif mas[3] == 'blade':
                if mas[2] == 1995:
                    return 7
                elif mas[2] == 1999:
                    return 8
    elif mas[1] == 1988:
        if mas[3] == 'flux':
            return 5
        elif mas[3] == 'red':
            if mas[4] == 2003:
                return 1
            elif mas[4] == 2012:
                return 0
        elif mas[3] == 'blade':
            if mas[0] == 'abnf':
                return 2
            elif mas[0] == 'kit':
                if mas[4] == 2012:
                    return 3
                elif mas[4] == 2003:
                    return 4


def f22(number):
    a = number & 0b00000000000000000000000000000001
    b = number & 0b00000000000000000000011111111110
    c = number & 0b00000000000000111111100000000000
    d = number & 0b00000111111111000000000000000000
    e = number & 0b00111000000000000000000000000000
    f = number & 0b11000000000000000000000000000000
    d = d >> 18
    e = e >> 27
    f = f >> 30
    c = c >> 11
    b = b >> 1
    numb = (d << 23) | (e << 20) | (f << 18) | (a << 17) | (b << 7) | c
    return numb


def f23(table1):
    result = re.findall(r'[\n]', table1)
    i = 0
    j = 0
    while i < len(result):
        j = i + 1
        while j < len(result):
            if i != 0:
                one = table1[27 * i:26 + (26 * (i)) + i]
                two = table1[27 * (j):26 + (27 * (j))]
                if one == two:
                    table1 = table1[:27 * (j)] + table1[26 + (26 * (j + 1))]
                    j -= 1
                    result = re.findall(r'[\n]', table1)
                j += 1
            else:
                one = table1[27 * i:26]
                two = table1[27 * (j):26 + (27 * (j)):]
                if one == two:
                    table1 = table1[:27 * (j)] + table1[26 + (26 * (j + 1))]
                    result = re.findall(r'[\n]', table1)
                    j -= 1
                j += 1
        i += 1
    table1 = table1.replace('None ', '')
    table1 = table1.replace('\n', '')
    while table1.find('!') != -1:
        result = re.search(r'[0-9]', table1)
        if table1[table1.find('!') + 1] == '0':
            table1 = table1[:result.start()] + "Не выполнено         " + table1[result.start():]
            table1 = table1[:table1.find('!')] + table1[(table1.find('!') + 2):]
        else:
            table1 = table1[:result.start()] + "Выполнено          " + table1[result.start():]
            table1 = table1[:table1.find('!')] + table1[(table1.find('!') + 2):]
    result = re.search(r'[0-9]', table1)
    table1 = table1[:result.start()] + "\n" + table1[result.start():]
    while table1.find('-') != -1:
        buff = table1[table1.find('-') + 4:table1.find('-') + 8] + '/' + table1[table1.find('-') + 1:table1.find(
            '-') + 3] + '/' + table1[table1.find('-') - 2:table1.find('-')] + "          "
        table1 = table1[:table1.find('-') - 2] + buff + '' + table1[(table1.find('-') + 8):]
    while table1.rfind('%') != -1:
        if table1[table1.find('%') - 2] == '0':
            table1 = table1.replace("100%", "1.0")
        else:
            n = round((int(table1[table1.find('%') - 2]) * 10 + int(table1[table1.find('%') - 1])) / 100, 1)
            table1 = table1 + str(n) + "                 "
            table1 = table1[:table1.find('%') - 2] + table1[table1.find('%') + 1:]
    table1 = table1[:table1.rfind('/') + 3] + "\n" + table1[table1.rfind('/') + 12:]
    return table1
