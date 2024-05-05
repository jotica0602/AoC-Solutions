import re

def parse(number_string: str, flag = False):
    if flag:
        number_string = number_string[::-1]
    if number_string == 'one':
        number_string = '1'
    elif number_string == 'two':
        number_string = '2'
    elif number_string == 'three':
        number_string = '3'
    elif number_string == 'four':
        number_string = '4'
    elif number_string == 'five':
        number_string = '5'
    elif number_string == 'six':
        number_string = '6'
    elif number_string == 'seven':
        number_string = '7'
    elif number_string == 'eight':
        number_string = '8'
    elif number_string == 'nine':
        number_string = '9'
    return number_string

with open('desktop/aoc/trebuchet/input2.txt') as file:
    text = file.read()
    lines = text.split()
    
pattern1 = r'1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'
pattern2 = pattern1[::-1]

ans = 0
for line in lines:
    first = parse(re.search(pattern1,line).group())
    line = line[::-1]
    last = parse(re.search(pattern2,line).group(),True)        
    ans += int(first + last)
    
print(ans)