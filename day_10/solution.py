import re as regex
import os
import sys

current_dir = os.path.dirname(__file__)
input = current_dir + '/input.txt'

with open(input) as file:
    text = file.read()

class Pipe(object):
    def __init__(self, kind:str, x, y) -> None:
        self.kind = kind
        self.pos = (x,y)
        if kind == '|':
            self.childs = [(x - 1, y), (x + 1, y)]
        elif kind == '-':
            self.childs = [(x, y - 1), (x, y + 1)]
        elif kind == 'L':
            self.childs = [(x - 1, y), (x, y + 1)]
        elif kind == 'J':
            self.childs = [(x - 1, y), (x, y - 1)]
        elif kind == '7':
            self.childs = [(x + 1, y), (x, y - 1)]
        elif kind == 'F':
            self.childs = [(x + 1, y), (x, y + 1)]
        elif kind == '.':
            self.childs = [(-1,-1), (-1,-1)]
        else:
            self.childs = [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]

    def __repr__(self) -> str:
        return self.kind

        
def print_map(map):
    n = len(map)
    for i in range(n):
        for j in range(n):
            print(map[i][j],sep=' ', end='')
        print()

n = 0
for i in range(len(text)):
    if text[i] == '\n':
        n = i
        break

map = [['' for _ in range(n)] for _ in range(n)]

text = text.replace('\n','') 
index = 0
start = 0

for i in range(n):
    for j in range(n):
        if text[index] == 'S':
            start = (i,j)
        map[i][j] = Pipe(text[index], i, j)
        index += 1

def is_valid(x,y,n):
    return x >= 0 or x < n or y >= 0 or y < n

def bfs(map, n, pipe:Pipe):
    q = [pipe]
    d = [[-1 for _ in range(n)] for _ in range(n)]
    d[pipe.pos[0]][pipe.pos[1]] = 0

    while q:
        v = q.pop(0)
        current_x, current_y = v.pos[0], v.pos[1]
        for child in v.childs:
            child_x, child_y = child[0], child[1]
            next_pipe = map[child_x][child_y]
            if is_valid(child_x, child_y, n) and d[child_x][child_y] == -1 and can_access(current_x, current_y, next_pipe):
                d[child_x][child_y] = d[current_x][current_y] + 1 
                q.append(next_pipe)
    
    max_d = 0
    for i in range(n):
        for j in range(n):
            max_d = max(max_d,d[i][j])
    return max_d

def can_access(x, y, child_pipe:Pipe):
    for child in child_pipe.childs:
        if child[0] == x and child[1] == y:
            return True
    return False

def solve_part1(map, n, start):
    s = map[start[0]][start[1]]
    return bfs(map, n, s)

# def solve_part2(map, n, start):
#     s = map[start[0]][start[1]]
#     return bfs(map, n, s)

print(solve_part1(map, n, start))
# print(solve_part2(map, n, start))