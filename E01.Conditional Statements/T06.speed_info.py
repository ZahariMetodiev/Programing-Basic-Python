speed = float(input())
output = ''

if speed <= 10:
    output = 'slow'
elif 10 < speed <= 50:
    output = 'average'
elif 50 < speed <= 150:
    output = 'fast'
elif 150 < speed <= 1000:
    output = 'ultra fast'
else:
    output = 'extremely fast'

print(output)
