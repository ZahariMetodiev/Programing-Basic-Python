country = input()
device = input()
difficulty = 0
performance = 0
if country == "Russia":
    if device == "ribbon":
        difficulty = 9.1
        performance = 9.4
    elif device == "hoop":
        difficulty = 9.3
        performance = 9.8
    elif device == "rope":
        difficulty = 9.6
        performance = 9
elif country == "Bulgaria":
    if device == "ribbon":
        difficulty = 9.6
        performance = 9.4
    elif device == "hoop":
        difficulty = 9.55
        performance = 9.75
    elif device == "rope":
        difficulty = 9.5
        performance = 9.4
elif country == "Italy":
    if device == "ribbon":
        difficulty = 9.2
        performance = 9.5
    elif device == "hoop":
        difficulty = 9.45
        performance = 9.35
    elif device == "rope":
        difficulty = 9.7
        performance = 9.15
grade = difficulty + performance
point = 20 - grade
percent = point / 20 * 100
print(f"The team of {country} get {grade:.3f} on {device}.")
print(f"{percent:.2f}%")
