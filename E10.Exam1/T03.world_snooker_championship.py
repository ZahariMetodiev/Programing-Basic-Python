stage = input()
ticket_type = input()
number_of_ticket = int(input())
photo = input()
price_per_ticket = 0
flag = True
if stage == "Quarter final":
    if ticket_type == "Standard":
        price_per_ticket = 55.5
    elif ticket_type == "Premium":
        price_per_ticket = 105.2
    elif ticket_type == "VIP":
        price_per_ticket = 118.9
elif stage == "Semi final":
    if ticket_type == "Standard":
        price_per_ticket = 75.88
    elif ticket_type == "Premium":
        price_per_ticket = 125.22
    elif ticket_type == "VIP":
        price_per_ticket = 300.4
elif stage == "Final":
    if ticket_type == "Standard":
        price_per_ticket = 110.1
    elif ticket_type == "Premium":
        price_per_ticket = 160.66
    elif ticket_type == "VIP":
        price_per_ticket = 400
total_price = price_per_ticket * number_of_ticket
if total_price > 4000:
    total_price *= 0.75
    flag = False
elif total_price > 2500:
    total_price *= 0.9
if photo == "Y" and flag:
    total_price += 40 * number_of_ticket
print(f"{total_price:.2f}")
