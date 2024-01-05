budget = float(input())
number_of_statist = int(input())
price_for_clothing = float(input())

decor = budget * 0.10
total_price_for_clothing = price_for_clothing * number_of_statist

if number_of_statist > 150:
    total_price_for_clothing *= 0.90

total_price_for_film = decor + total_price_for_clothing

if total_price_for_film <= budget:
    print("Action!")
    print(f'Wingard starts filming with {budget - total_price_for_film:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {total_price_for_film - budget:.2f} leva more.')
