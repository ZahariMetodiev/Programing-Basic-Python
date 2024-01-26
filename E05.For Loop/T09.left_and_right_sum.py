n = int(input())

left_sum = 0
right_sum = 0

for _ in range(n):
    number = int(input())
    left_sum += number

for _ in range(n):
    number = int(input())
    right_sum += number

if right_sum == left_sum:
    print(f'Yes, sum = {right_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')
    