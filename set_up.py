import os
import re

current_directory = os.path.dirname(__file__)
print(current_directory)
pattern = r'\d+'

files = [file for file in os.listdir(current_directory) if os.path.isdir(file)]

if len(files) == 0:
    os.mkdir(current_directory + '/day_1')

else:
    days = []
    
    for file in files:
        match = re.search(pattern,file)
        if match:
            days.append(int(match[0]))
            
    days.sort()
    last_day_number = str(days[len(days)-1] + 1)

    new_folder = current_directory + '/' + 'day_' + last_day_number
    os.mkdir(new_folder)
        
print('end')