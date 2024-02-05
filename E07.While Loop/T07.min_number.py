import sys

data = input()
min_number = sys.maxsize

while data != "Stop":
    number = int(data)
    if number < min_number:
        min_number = number

    data = input()

print(min_number)
