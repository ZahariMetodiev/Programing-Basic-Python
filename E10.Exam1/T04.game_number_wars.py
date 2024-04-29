first_player = input()
second_player = input()
command = input()
first_player_point = 0
second_player_point = 0
while command != "End of game":
    first_player_card = int(command)
    second_player_card = int(input())
    if first_player_card > second_player_card:
        first_player_point += first_player_card - second_player_card
    elif second_player_card > first_player_card:
        second_player_point += second_player_card - first_player_card
    else:
        print("Number wars!")
        first_player_card = int(input())
        second_player_card = int(input())
        if first_player_card > second_player_card:
            print(f"{first_player} is winner with {first_player_point} points")
        else:
            print(f"{second_player} is winner with {second_player_point} points")
        exit()
    command = input()
print(f"{first_player} has {first_player_point} points")
print(f"{second_player} has {second_player_point} points")
