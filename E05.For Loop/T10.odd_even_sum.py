n = int(input())

odd_position_sum = 0
even_position_sum = 0

for i in range(n):
    number = int(input())

    if i % 2 == 0:
        even_position_sum += number
    else:
        odd_position_sum += number

if odd_position_sum == even_position_sum:
    print('Yes')
    print(f'Sum = {even_position_sum}')
else:
    print('No')
    print(f"Diff = {abs(even_position_sum - odd_position_sum)}")
