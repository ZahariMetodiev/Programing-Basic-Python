day = input()
output = ''

if day == 'Monday':
    output = 'Working day'
elif day == 'Tuesday':
    output = 'Working day'
elif day == 'Wednesday':
    output = 'Working day'
elif day == 'Thursday':
    output = 'Working day'
elif day == 'Friday':
    output = 'Working day'
elif day == 'Saturday':
    output = 'Weekend'
elif day == 'Sunday':
    output = 'Weekend'
else:
    output = 'Error'

print(output)
