import re
import sys
with open('input.txt') as file:
    text = file.read()
    lines = text.split(sep='\n')

pattern = r'\d+'
seeds = [int(x) for x in re.findall(pattern,lines[0])]
result = sys.maxsize

def map(x,a,b,c) -> tuple[int,bool]:
    if x < b or x > b + c - 1: 
        return (x, False)
    else: 
        return (x - b + a, True)
     
for seed in seeds:
    plot = (seed, False)
    for i in range(1,len(lines)):
        if lines[i] == '' or lines[i][0].isalpha():
            plot = (plot[0], False)
        elif not plot[1]:
            ranges = [int(x) for x in re.findall(pattern,lines[i])]
            plot = map(plot[0], ranges[0], ranges[1], ranges[2])
        if i == len(lines) - 1:
            # print(f'location: {plot[0]}')
            result = min(result, plot[0])
            
print(result)
print('end')