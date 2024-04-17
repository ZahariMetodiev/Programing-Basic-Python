start = int(input())
end = int(input())
magic_number = int(input())
combination_counter = 0
flag = False
for first in range(start, end + 1):
    for second in range(start, end + 1):
        combination_counter += 1
        if first + second == magic_number:
            print(f"Combination N:{combination_counter} ({first} + {second} = {magic_number})")
            exit()
print(f"{combination_counter} combinations - neither equals {magic_number}")

