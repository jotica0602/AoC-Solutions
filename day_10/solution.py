import os
import sys
sys.setrecursionlimit(15000)
current_dir = os.path.dirname(__file__)
input = current_dir + '/input.txt'
n = 0
with open(input) as file:
    text = file.read()

n = len(text.split('\n'))

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
    m = len(map[0])
    for i in range(n):
        for j in range(m):
            print(f'{map[i][j]}', end=' ', flush= [True])
        print()

m = 0
for i in range(len(text)):
    if text[i] == '\n':
        m = i
        break

map = [['' for _ in range(m)] for _ in range(n)]

text = text.replace('\n','') 
index = 0
start = 0

for i in range(n):
    for j in range(m):
        if text[index] == 'S':
            start = (i,j)
        map[i][j] = Pipe(text[index], i, j)
        index += 1

def is_valid(x,y,n,m):
    return x >= 0 and x < n and y >= 0 and y < m

def bfs(map, n, m, pipe:Pipe):
    q = [pipe]
    d = [[-1 for _ in range(m)] for _ in range(n)]
    c = [['w' for _ in range (m)] for _ in range(n)]
    d[pipe.pos[0]][pipe.pos[1]] = 0
    polygon = []

    while q:
        v = q.pop(0)
        current_x, current_y = v.pos[0], v.pos[1]
        polygon.append((current_x, current_y))
        for child in v.childs:
            child_x, child_y = child[0], child[1]
            next_pipe = map[child_x][child_y]
            if is_valid(child_x, child_y, n, m) and d[child_x][child_y] == -1 and can_access(current_x, current_y, next_pipe):
                d[child_x][child_y] = d[current_x][current_y] + 1 
                c[child_x][child_y] = 'b'
                q.append(next_pipe)


    max_d = 0
    for i in range(n):
        for j in range(m):
            max_d = max(max_d,d[i][j])

    # print_map(d)
    return max_d, d, polygon

def dfs(map, n, m, start:Pipe):
    polygon = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    polygon.append((start.pos[0],start.pos[1]))

    def dfs_visit(pipe:Pipe):
        visited[pipe.pos[0]][pipe.pos[1]] = True
        current_x, current_y = pipe.pos[0], pipe.pos[1]
        for child in pipe.childs:
            child_x, child_y = child[0], child[1]
            if is_valid(child_x, child_y, n, m):
                next_pipe = map[child_x][child_y]
                if not visited[child_x][child_y]: 
                    if can_access(current_x, current_y, next_pipe):
                        polygon.append((child_x,child_y))
                        dfs_visit(next_pipe)

    dfs_visit(start)
    return polygon, visited

def can_access(x, y, child_pipe:Pipe):
    for child in child_pipe.childs:
        if child[0] == x and child[1] == y:
            return True
    return False

def is_inside(edges, xp, yp):
    cnt = 0
    n = len(edges)
    for i in range(n):
        (x1, y1), (x2, y2) = edges[i], edges[(i + 1) % n]
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp-y1)/(y2-y1))*(x2-x1):
            cnt += 1
    return 1 if cnt%2 == 1 else 0

def solve_part1(map, n, m, start):
    s = map[start[0]][start[1]]
    return bfs(map, n, m, s)[0]

def solve_part2(map, n, m, start):
    s = map[start[0]][start[1]]
    unwrap = dfs(map, n, m, s)
    polygon, visited = unwrap[0], unwrap[1]
    ans = 0
    for i in range (n):
        for j in range(m):
            if not visited[i][j]:
                ans += is_inside(polygon,i,j)
    return ans

print(solve_part1(map, n, m, start))
print(solve_part2(map, n, m, start))