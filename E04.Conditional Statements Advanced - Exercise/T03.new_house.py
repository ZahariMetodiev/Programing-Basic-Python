flower_type = input()
flower_numbers = int(input())
budget = int(input())

roses_price = 5
dahlias_price = 3.8
tulips_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5

total_price = 0
if flower_type == 'Roses':
    total_price = roses_price * flower_numbers
    if flower_numbers > 80:
        total_price *= 0.90
elif flower_type == 'Dahlias':
    total_price = dahlias_price * flower_numbers
    if flower_numbers > 90:
        total_price *= 0.85
elif flower_type == 'Tulips':
    total_price = tulips_price * flower_numbers
    if flower_numbers > 80:
        total_price *= 0.85
elif flower_type == 'Narcissus':
    total_price = narcissus_price * flower_numbers
    if flower_numbers < 120:
        total_price *= 1.15
elif flower_type == 'Gladiolus':
    total_price = gladiolus_price * flower_numbers
    if flower_numbers < 80:
        total_price *= 1.20

if budget >= total_price:
    print(f'Hey, you have a great garden with {flower_numbers} {flower_type} and {budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money, you need {total_price - budget:.2f} leva more.')