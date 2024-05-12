import re
import os
current_dir = os.path.dirname(__file__)
input = current_dir + '/input.txt'

with open(input) as file:
    lines = file.read().split('\n')
    
pattern = r'-?\d+'
sequences = [[int(num) for num in re.findall(pattern,lines[i])] for i in range(len(lines))]

def is_a_zero_seq(seq:list[int]):
    for num in seq:
        if num != 0:
            return False
        
    return True

def solve(seq:list[int]):
    if is_a_zero_seq(seq):
        return 0
    else:
        new_seq = []
        for i in range(len(seq)-1):
            new_seq.append(seq[i+1] - seq[i])
        return seq[len(seq)-1] + solve(new_seq)
    
ans = 0
for sequence in sequences:
    ans += solve(sequence)

print(sequences.__len__())
print(ans)
print('end')

    