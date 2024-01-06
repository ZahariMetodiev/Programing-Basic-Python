age = float(input())
gender = input()
tittle = ''

if gender == 'm':
    if age < 16:
        tittle = 'Master'
    else:
        tittle = 'Mr.'
elif gender == 'f':
    if age < 16:
        tittle = 'Miss'
    else:
        tittle = 'Ms.'

print(tittle)
