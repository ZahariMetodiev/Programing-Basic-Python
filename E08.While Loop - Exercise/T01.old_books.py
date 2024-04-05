searched_book = input()
counter = 0

data = input()

while data != searched_book and data != "No More Books":
    counter += 1
    data = input()

if data == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
else:
    print(f"You checked {counter} books and found it.")
