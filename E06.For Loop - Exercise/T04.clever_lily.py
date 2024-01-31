age = int(input())
laundry_price = float(input())
toy_price = int(input())
toy_counter = 0
money = 0
total_money = 0
brother_money = 0

for i in range(1, age + 1):
    money += 5
    if i % 2 == 0:
        total_money += money - 1

    else:
        toy_counter += 1

total_toy_price = toy_counter * toy_price
total_money += total_toy_price

if total_money >= laundry_price:
    print(f'Yes! {total_money - laundry_price:.2f}')
else:
    print(f'No! {laundry_price - total_money:.2f}')
