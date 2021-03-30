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


# def f22(number):
#     a = number & 0b00000000000000000000000000000001
#     b = number & 0b00000000000000000000011111111110
#     c = number & 0b00000000000000111111100000000000
#     d = number & 0b00000111111111000000000000000000
#     e = number & 0b00111000000000000000000000000000
#     f = number & 0b11000000000000000000000000000000
#     d = d >> 18
#     e = e >> 27
#     f = f >> 30
#     c = c >> 11
#     b = b >> 1
#     numb = (d << 23) | (e << 20) | (f << 18) | (a << 17) | (b << 7) | c
#     return numb

# def f22(number):
#     a = number & 0b00000000000000000000000000000001
#     print("a",bin(a))
#     b = number & 0b00000000000000000000000000000010
#     print("b",bin(b))
#     c = number & 0b00000000000000000000000001111100
#     print("c",bin(c))
#     d = number & 0b00000000000000000000001110000000
#     print("d",bin(d))
#     e = number & 0b00000000000000000001110000000000
#     print("e",bin(e))
#     f = number & 0b00000000111111111110000000000000
#     print("f",bin(f))
#     g = number & 0b11111110000000000000000000000000
#     print("g",bin(g))
#     numb = (b << 30) | (d << 19) | (g >> 5) | (e << 5) | (c << 10) | (a << 11) | (f >> 14)
#     return bicn(numb)
def f22(number):
    a = number & 0b00000000000000000000000000000001
    b = number & 0b00000000000000000000000000000010
    c = number & 0b00000000000000000000000011111100
    d = number & 0b00000000000000000000011100000000
    e = number & 0b00000000000000000011100000000000
    f = number & 0b00000001111111111100000000000000
    g = number & 0b11111110000000000000000000000000
    numb = (b << 30) | (d << 19) | (g >> 5) | (e << 6) | (c << 10) | (a << 11) | (f >> 14)
    return numb


def f23(table1):
    table2 = []
    line1 = []
    line2 = []
    line3 = []
    check = False
    for i in range(len(table1)):
        for l in range(len(line1)):
            if table1[i][0][table1[i][0].find('!'):] == line1[l]:
                if table1[i][0][:table1[i][0].find('!')] == line2[l]:
                    if table1[i][3] == line3[l]:
                        check = True
        if not check:
            for j in range(4):
                if table1[i][j] is not None:
                    if table1[i][j].find('!') != -1:
                        line1.append(table1[i][j][table1[i][j].find('!'):])
                        line2.append(table1[i][j][:table1[i][j].find('!')])
                    if table1[i][j].find('%') != -1:
                        line3.append(table1[i][j])
        check=False
    for l in range(len(line1)):
        if line1[l] == '!0':
            line1[l] = "Не выполнено"
        else:
            line1[l] = "Выполнено"
    for l in range(len(line3)):
        line3[l] = str(round(int(line3[l][:line3[l].find('%')]) / 100, 1))
    for l in range(len(line2)):
        line2[l]=str(line2[l][line2[l].rfind('-')+1:]+'/'+line2[l][line2[l].find('-')+1:line2[l].rfind('-')]+'/'+line2[l][:line2[l].find('-')])
    table2 = [line1, line2, line3]
    return table2

print (bin(f22(3847250330)) == bin(2401920321))
print(bin(2401920321))