text = input()
output = 0

for char in text:
    if char == 'a':
        output += 1
    elif char == 'e':
        output += 2
    elif char == 'i':
        output += 3
    elif char == 'o':
        output += 4
    elif char == 'u':
        output += 5

print(output)
