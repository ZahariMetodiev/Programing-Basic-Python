total_sum = 0

data = input()

while data != "NoMoreMoney":
    number = float(data)
    if number < 0:
        print("Invalid operation!")
        break
    total_sum += number
    print(f"Increase: {number:.2f}")
    data = input()

print(f"Total: {total_sum:.2f}")
