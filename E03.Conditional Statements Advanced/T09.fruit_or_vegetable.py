data = input()
output = ''

if data == 'banana' or data == 'apple' or data == 'kiwi' or data == 'cherry' or data == 'lemon' or data == 'grapes':
    output = 'fruit'
elif data == 'tomato' or data == 'cucumber' or data == 'pepper' or data == 'carrot':
    output = 'vegetable'
else:
    output = 'unknown'

print(output)
