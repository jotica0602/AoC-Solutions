import re
with open('input.txt') as file:
    lines = file.readlines()

pattern = r'\d+'
times, distances = [x for x in re.findall(pattern,lines[0])], [x for x in re.findall(pattern,lines[1])]

real_time = ''
real_distance = ''

for time in times:
    real_time += time

for distance in distances:
    real_distance += distance

real_time = int(real_time)
real_distance = int(real_distance)

def solve(time,distance) -> int:
    how_many_ways = 0
    for i in range(0,time):
        if i*(time-i) > distance:
            how_many_ways += 1
    return how_many_ways
    
ans = solve(real_time,real_distance)

print(ans)
print('end')
