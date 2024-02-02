number_of_groups = int(input())

total_people = 0
musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(number_of_groups):
    number_of_people = int(input())
    total_people += number_of_people

    if number_of_people <= 5:
        musala += number_of_people
    elif number_of_people <= 12:
        montblanc += number_of_people
    elif number_of_people <= 25:
        kilimanjaro += number_of_people
    elif number_of_people <= 40:
        k2 += number_of_people
    elif number_of_people >= 41:
        everest += number_of_people

musala_percent = musala / total_people * 100
montblanc_percent = montblanc / total_people * 100
kilimanjaro_percent = kilimanjaro / total_people * 100
k2_percent = k2 / total_people * 100
everest_percent = everest / total_people * 100

print(f"{musala_percent:.2f}%")
print(f"{montblanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")

