import math

record = float(input())
distance = float(input())
time_for_meter = float(input())

time = distance * time_for_meter
delay = math.floor((distance / 15)) * 12.5
total_time = time + delay

if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_time - record:.2f} seconds slower.')
    