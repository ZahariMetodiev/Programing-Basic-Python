import math

first_time = int(input())
second_time = int(input())
thirt_time = int(input())

total_time = first_time + second_time + thirt_time
minutes = math.floor(total_time / 60)
seconds = total_time % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
    