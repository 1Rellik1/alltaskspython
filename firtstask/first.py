from math import sqrt, tan, log1p, cos, fabs, e


def f(x, y, z):
    return sqrt(28 * x ** 7 - z ** 5 - 40) - sqrt((z ** 2 - x ** 4) / (tan(z) + 19 * x ** 8 + 59)) - (
            (72 * x ** 6 + z ** 5 + 77) / (z ** 3 + y ** 7 + 47))


def f2(x):
    if x < 122:
        return log1p(28 * x ** 6) - x ** 8
    elif 122 <= x < 221:
        return (cos(x) - 44 * x ** 3) ** 5 - 49 * x ** 3
    else:
        return x ** 5 - x ** 3


def f3(n, m):
    summ1 = 0
    summ2 = 0
    for i in range(1, n):
        for j in range(1, m):
            summ1 += (i ** 2 - j ** 8)
    for i in range(1, n):
        summ2 += (e ** i + tan(i) - 7)
    return (11*summ1) + (summ2 / 26)


def f4(x):
    if x == 1 or x == 0:
        return 4
    else:
        return tan(f4(x - 1)) - fabs(f4(x - 2))


print("{:.2e}".format(f(1, 11, -70)))
print("{:.2e}".format(f2(201)))
print("{:.2e}".format(f3(68, 45)))
print("{:.2e}".format(f4(11)))
