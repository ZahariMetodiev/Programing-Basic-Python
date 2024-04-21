won_counter = 0
lost_counter = 0
draw_counter = 0
for game in range(3):
    data = input()
    x = data[0]
    y = data[2]
    if x > y:
        won_counter += 1
    elif y > x:
        lost_counter += 1
    else:
        draw_counter += 1
print(f"Team won {won_counter} games.")
print(f"Team lost {lost_counter} games.")
print(f"Drawn games: {draw_counter}")
