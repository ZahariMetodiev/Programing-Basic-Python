import math

tennis_racket_price = float(input())
number_of_tennis_racket = int(input())
number_of_sneakers = int(input())
total_price_for_racket = tennis_racket_price * number_of_tennis_racket
total_price_for_sneakers = (tennis_racket_price / 6) * number_of_sneakers
equipment = (total_price_for_sneakers + total_price_for_racket) * 0.2
total_price = total_price_for_sneakers + total_price_for_racket + equipment
djokovic_paid = total_price / 8
sponsor_paid = total_price * 7 / 8
print(f"Price to be paid by Djokovic {math.floor(djokovic_paid)}")
print(f"Price to be paid by sponsors {math.ceil(sponsor_paid)}")
