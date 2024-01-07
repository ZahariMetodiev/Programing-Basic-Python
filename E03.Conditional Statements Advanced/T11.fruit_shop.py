product = input()
day_of_week = input()
quantity = float(input())

price = 0

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
        or day_of_week == 'Thursday' or day_of_week == 'Friday':
    if product == 'banana':
        price = 2.5
    elif product == 'apple':
        price = 1.2
    elif product == 'orange':
        price = 0.85
    elif product == 'grapefruit':
        price = 1.45
    elif product == 'kiwi':
        price = 2.7
    elif product == 'pineapple':
        price = 5.5
    elif product == 'grapes':
        price = 3.85
elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if product == 'banana':
        price = 2.7
    elif product == 'apple':
        price = 1.25
    elif product == 'orange':
        price = 0.90
    elif product == 'grapefruit':
        price = 1.60
    elif product == 'kiwi':
        price = 3
    elif product == 'pineapple':
        price = 5.6
    elif product == 'grapes':
        price = 4.20

total_price = price * quantity

if price == 0:
    print('error')
else:
    print(f'{total_price:.2f}')

