actor_name = input()
point_from_academy = float(input())
number_of_evaluators = int(input())

total_points = 0

for _ in range(number_of_evaluators):
    evaluators_name = input()
    current_point = float(input())

    total_points += point_from_academy + ((len(evaluators_name) * current_point) / 2)

    if total_points == 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - total_points} more!")
