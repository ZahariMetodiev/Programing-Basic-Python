budget = float(input())
season = input()

holiday_type = ''
destination = ''
spend_money = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        spend_money = budget * 0.30
    elif season == 'winter':
        spend_money = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        spend_money = budget * 0.40
    elif season == 'winter':
        spend_money = budget * 0.80
else:
    destination = 'Europe'
    spend_money = budget * 0.90

if season == 'summer' and destination != 'Europe':
    holiday_type = 'Camp'
else:
    holiday_type = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{holiday_type} - {spend_money:.2f}')