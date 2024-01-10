month = input()
number_of_nights = int(input())

apartment_price = 0
studio_price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
elif month == 'June' or month == 'September':
    studio_price = 75.2
    apartment_price = 68.7
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

if number_of_nights > 14:
    apartment_price *= 0.90
    if month == 'May' or month == 'October':
        studio_price *= 0.70
    elif month == 'June' or month == 'September':
        studio_price *= 0.80
elif 7 < number_of_nights <= 14:
    if month == 'May' or month == 'October':
        studio_price *= 0.95

total_apartment_price = apartment_price * number_of_nights
total_studio_price = studio_price * number_of_nights

print(f'Apartment: {total_apartment_price:.2f} lv.')
print(f'Studio: {total_studio_price:.2f} lv.')