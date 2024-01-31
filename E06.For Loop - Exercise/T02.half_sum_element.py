import sys

n = int(input())
max_num = -sys.maxsize
sum = 0

for _ in range(n):
    number = int(input())
    if number > max_num:
        max_num = number
    sum += number

if max_num == sum - max_num:
    print('Yes')
    print(f'Sum = {sum - max_num}')
else:
    print('No')
    print(f'Diff = {abs(max_num - (sum - max_num))}')


