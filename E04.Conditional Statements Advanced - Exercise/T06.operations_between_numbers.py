first_number = int(input())
second_number = int(input())
operator = input()
result = 0

if (operator == '/' or operator == '%') and second_number == 0:
    print(f'Cannot divide {first_number} by zero')
else:
    if operator == '+' or operator == '-' or operator == '*':
        even_or_odd = ''
        if operator == '+':
            result = first_number + second_number
        elif operator == '-':
            result = first_number - second_number
        elif operator == '*':
            result = first_number * second_number
        if 2 != 0:
            even_or_odd = 'odd'
        else:
            even_or_odd = 'even'

        print(f'{first_number} {operator} {second_number} = {result} - {even_or_odd}')
    elif operator == '/':
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {first_number / second_number:.2f}")
    elif operator == '%':
        print(f'{first_number} % {second_number} = {first_number % second_number}')
