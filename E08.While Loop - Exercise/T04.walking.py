goal = 10000
total_steps = 0
data = input()

while data != "Going home":
    current_steps = int(data)
    total_steps += current_steps
    if total_steps >= 10000:
        break
    data = input()
if data == "Going home":
    step_to_home = int(input())
    total_steps += step_to_home
different = abs(total_steps - 10000)
if total_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{different} steps over the goal!")
else:
    print(f"{different} more steps to reach goal.")
