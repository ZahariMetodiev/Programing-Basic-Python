number_of_tabs = int(input())
salary = int(input())

facebook = 150
instagram = 100
reddit = 50

for _ in range(number_of_tabs):
    website = input()

    if website == 'Facebook':
        salary -= facebook
    elif website == 'Instagram':
        salary -= instagram
    elif website == 'Reddit':
        salary -= reddit

    if salary <= 0:
        print('You have lost your salary.')
        break

if salary > 0:
    print(salary)
