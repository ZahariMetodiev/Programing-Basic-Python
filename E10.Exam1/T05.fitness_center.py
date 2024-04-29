visitors = int(input())
back_counter = 0
chest_counter = 0
legs_counter = 0
abs_counter = 0
protein_shake = 0
protein_bar = 0
work_out_counter = 0
protein_counter = 0
for _ in range(visitors):
    activity = input()
    if activity == "Back":
        back_counter += 1
        work_out_counter += 1
    elif activity == "Chest":
        chest_counter += 1
        work_out_counter += 1
    elif activity == "Legs":
        legs_counter += 1
        work_out_counter += 1
    elif activity == "Abs":
        abs_counter += 1
        work_out_counter += 1
    elif activity == "Protein shake":
        protein_shake += 1
        protein_counter += 1
    elif activity == "Protein bar":
        protein_bar += 1
        protein_counter += 1
work_out_percent = work_out_counter / visitors * 100
protein_percent = protein_counter / visitors * 100
print(f"{back_counter} - back")
print(f"{chest_counter} - chest")
print(f"{legs_counter} - legs")
print(f"{abs_counter} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{work_out_percent:.2f}% - work out")
print(f"{protein_percent:.2f}% - protein")
