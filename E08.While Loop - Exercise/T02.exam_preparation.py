poor_grades = int(input())
poor_grade_counter = 0
problem_counter = 0
sum_grade = 0
data = input()

while data != "Enough":
    problem_name = data
    grade = int(input())
    problem_counter += 1
    sum_grade += grade

    if grade <= 4:
        poor_grade_counter += 1
        if poor_grade_counter >= poor_grades:
            print(f"You need a break, {poor_grade_counter} poor grades.")

    data = input()

print(f"Average score: {sum_grade / problem_counter :.2f}")
print(f"Number of problems: {problem_counter}")
print(f"Last problem: {problem_name}")
