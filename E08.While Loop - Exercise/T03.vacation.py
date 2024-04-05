needed_money_for_excursion = float(input())
available_money = float(input())
spend_counter = 0
day_counter = 0

while available_money < needed_money_for_excursion and spend_counter < 5:
    day_counter += 1
    tape_of_action = input()
    amaunt = float(input())

    if tape_of_action == "spend":
        available_money -= amaunt
        spend_counter += 1
        if available_money < 0:
            available_money = 0
    elif tape_of_action == "save":
        available_money += amaunt
        spend_counter = 0

if spend_counter > 5:
    print("You can't save the money.")
    print(day_counter)

if available_money >= needed_money_for_excursion:
    print(f"You saved the money for {day_counter} days.")
