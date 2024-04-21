fee = int(input())
sneakers_price = fee * 0.60
kit_price = sneakers_price * 0.80
ball_price = kit_price / 4
accessories = ball_price / 5
total_price = fee + sneakers_price + kit_price + ball_price + accessories
print(f"{total_price:.2f}")
