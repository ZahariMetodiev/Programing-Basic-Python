import math

number = int(input())

for i in range(0, number + 1):
    if i % 2 == 0:
        print(f'{math.pow(2, i):g}')
