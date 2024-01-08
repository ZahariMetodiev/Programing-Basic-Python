budget = int(input())
season = input()
number_of_fisherman = int(input())

ship_price_spring = 3000
ship_price_summer_and_autumn = 4200
ship_price_winter = 2600
price = 0

if season == 'Spring':
    price = ship_price_spring
elif season == 'Autumn' or season == 'Summer':
    price = ship_price_summer_and_autumn
elif season == 'Winter':
    price = ship_price_winter

if number_of_fisherman <= 6:
    price *= 0.90
elif number_of_fisherman <= 11:
    price *= 0.85
elif number_of_fisherman > 12:
    price *= 0.75

if number_of_fisherman % 2 == 0 and season != 'Autumn':
    price *= 0.95

if budget >= price:
    print(f'Yes! You have {budget - price:.2f} leva left.')
else:
    print(f'Not enough money! You need {price - budget:.2f} leva.')
