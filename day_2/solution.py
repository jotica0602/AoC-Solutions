import os
import re

with open('input.txt') as file:
    text = file.read()

class Game:
    def __init__(self,number:int, isvalid:bool = True) -> None:
        self.number = number
        self.isvalid = isvalid

def update_validity(colors: tuple) -> bool:
    if colors[0] > 12 or colors[1] > 13 or colors[2] > 14:
        return False
    else:
        return True
        
def get_colors(game:Game, text:str) -> None:
    number, color, = '', ''
    red, green, blue = 0, 0, 0
    
    for char in text:
        if char.isdigit():
            number += char
        elif char.isalpha():
            color += char
        if color == 'red':
            red = max(int(number),red)
            number, color = '',''
        elif color == 'green':
            green = max(int(number),green)
            number, color = '',''
        elif color == 'blue':
            blue = max(int(number),blue)
            number, color = '',''
        if char == ';' or char == '\n':
            number, color, = '', ''
            
    return (red,green,blue)
            
games_list = []
pattern = r'\w+\s(\d+):\s((\d+\s\w+\,?\;?\s?\r?)*)'

parsed_lines = re.findall(pattern,text)
ans = 0

for line in parsed_lines:
    number = int(line[0])
    game = Game(number)
    nums = get_colors(game, line[1])
    nums = nums[0]*nums[1]*nums[2]
    ans += nums
    games_list.append(game)
    
# for game in games_list:
#     if game.isvalid:
#         ans += game.number

print(ans)