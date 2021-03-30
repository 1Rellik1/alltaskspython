import re

line = input()
subline = input()

a = [i for i in range(len(line)) if line.startswith(subline, i)]

for elem in a:
    print(elem, end=' ')
