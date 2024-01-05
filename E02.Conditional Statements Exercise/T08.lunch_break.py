import math

name_of_film = input()
episode_duration = int(input())
break_duration = int(input())

time_for_lunch = break_duration / 8
time_for_relax = break_duration / 4
time_rest = break_duration - time_for_relax - time_for_lunch

if time_rest >= episode_duration:
    print(f'You have enough time to watch {name_of_film} and left with '
          f'{math.ceil(time_rest - episode_duration)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {name_of_film}, you need '
          f'{math.ceil(episode_duration - time_rest)} more minutes.')

