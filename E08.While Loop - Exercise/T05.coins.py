change = float(input())
coins_counter = 0
converted_change = int(change * 100)

while converted_change > 0:
    if converted_change - 200 >= 0:
        coins_counter += 1
        converted_change -= 200
    elif converted_change - 100 >= 0:
        coins_counter += 1
        converted_change -= 100
    elif converted_change - 50 >= 0:
        coins_counter += 1
        converted_change -= 50
    elif converted_change - 20 >= 0:
        coins_counter += 1
        converted_change -= 20
    elif converted_change - 10 >= 0:
        coins_counter += 1
        converted_change -= 10
    elif converted_change - 5 >= 0:
        coins_counter += 1
        converted_change -= 5
    elif converted_change - 2 >= 0:
        coins_counter += 1
        converted_change -= 2
    elif converted_change - 1 >= 0:
        coins_counter += 1
        converted_change -= 1

print(coins_counter)




