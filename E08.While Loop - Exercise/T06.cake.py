piece_width = int(input())
piece_length = int(input())
number_of_pieces = piece_width * piece_length
data: str = input()
while data != "STOP":
    taken_peaces = int(data)
    number_of_pieces -= taken_peaces
    data = input()
    if number_of_pieces <= 0:
        break
if number_of_pieces > 0:
    print(f"{number_of_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(number_of_pieces)} pieces more.")
