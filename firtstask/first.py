from math import sqrt, tan, log1p, cos, fabs, e


def f11(x, y, z):
    return sqrt(28 * x ** 7 - z ** 5 - 40) - sqrt((z ** 2 - x ** 4) / (tan(z) + 19 * x ** 8 + 59)) - (
            (72 * x ** 6 + z ** 5 + 77) / (z ** 3 + y ** 7 + 47))


def f12(x):
    if x < 122:
        return log1p(28 * x ** 6) - x ** 8
    elif 122 <= x < 221:
        return (cos(x) - 44 * x ** 3) ** 5 - 49 * x ** 3
    else:
        return x ** 5 - x ** 3


def f13(n, m):
    summ1 = 0
    summ2 = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            summ1 += (i ** 2 - j ** 8)
    for i in range(1, n+1):
        summ2 += (e ** i + tan(i) - 7)
    return (11*summ1) + (summ2 / 26)


def f14(x):
    if x == 1 or x == 0:
        return 4
    else:
        return tan(f14(x - 1)) - fabs(f14(x - 2))

