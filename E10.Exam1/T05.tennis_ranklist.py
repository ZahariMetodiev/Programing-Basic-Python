import math

number_of_tournament = int(input())
start_point = int(input())
winning_point = 0
winning_tournament = 0
for _ in range(number_of_tournament):
    stage = input()
    current_point = 0
    if stage == "W":
        current_point = 2000
        winning_tournament += 1
    elif stage == "F":
        current_point = 1200
    elif stage == "SF":
        current_point = 720
    winning_point += current_point
final_point = winning_point + start_point
average_point = winning_point / number_of_tournament
percent_winning_tournament = winning_tournament / number_of_tournament * 100
print(f"Final points: {final_point}")
print(f"Average points: {math.floor(average_point)}")
print(f"{percent_winning_tournament:.2f}%")
