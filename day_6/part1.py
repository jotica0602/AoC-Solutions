import re
with open('input.txt') as file:
    lines = file.readlines()

pattern = r'\d+'
times, distances = [int(x) for x in re.findall(pattern,lines[0])], [int(x) for x in re.findall(pattern,lines[1])]

def solve(time,distance) -> int:
    how_many_ways = 0
    for i in range(0,time):
        if i*(time-i) > distance:
            how_many_ways += 1
    return how_many_ways
    
ans = solve(times[0],distances[0])

for i in range(1,len(times)):
    ans *= solve(times[i],distances[i])

print(ans)
print('end')
