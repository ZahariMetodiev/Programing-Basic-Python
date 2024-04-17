destination = input()
while destination != "End":
    needed_money = float(input())
    while needed_money > 0:
        current_money = float(input())
        needed_money -= current_money
    print(f"Going to {destination}!")
    destination = input()
