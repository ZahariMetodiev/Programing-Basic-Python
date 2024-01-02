excursion_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60
dolls_price = 3
bears_price = 4.10
minions_price = 8.20
trucks_price = 2

toys_count = puzzle_count + dolls_count + bears_count + minions_count + trucks_count
collected_money = puzzle_count * puzzle_price + dolls_count * dolls_price + bears_count * bears_price + \
minions_count * minions_price + trucks_count * trucks_price

if toys_count >= 50:
    collected_money *= 0.75

final_money = collected_money * 0.90

if collected_money >= excursion_price:
    print(f'Yes! {final_money - excursion_price:.2f} lv left.')
else:
    print(f'Not enough money! {excursion_price - final_money:.2f} lv needed.')