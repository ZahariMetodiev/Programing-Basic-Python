budget = float(input())
number_of_graphic_card = int(input())
number_of_processors = int(input())
number_of_RAM = int(input())

graphic_card_price = number_of_graphic_card * 250
processors_price =  number_of_processors * (graphic_card_price * 0.35)
RAM_price = number_of_RAM * (graphic_card_price * 0.10)
total_money = graphic_card_price + processors_price + RAM_price

if number_of_graphic_card > number_of_processors:
    total_money *= 0.85

if budget >= total_money:
    print(f'You have {budget - total_money:.2f} leva left!')
else:
    print(f'Not enough money! You need {total_money - budget:.2f} leva more!')
