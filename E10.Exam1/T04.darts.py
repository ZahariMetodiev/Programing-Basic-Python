name_of_player = input()
command = input()
start_point = 301
successful_shots = 0
failed_shots = 0
while command != "Retire":
    field = command
    points = int(input())
    current_point = 0
    if field == "Single":
        current_point = points
    elif field == "Double":
        current_point = points * 2
    elif field == "Triple":
        current_point = points * 3
    if start_point - current_point >= 0:
        successful_shots += 1
        start_point -= current_point
    else:
        failed_shots += 1
    if start_point == 0:
        print(f"{name_of_player} won the leg with {successful_shots} shots.")
        exit()
    command = input()
if command == "Retire":
    print(f"{name_of_player} retired after {failed_shots} unsuccessful shots.")
