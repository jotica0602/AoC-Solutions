with open('input1.txt') as file:
    text = file.readlines()
    
with open('input1.txt') as file: 
    txt = file.read()


def print_matrix(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            print(f'{text_matrix[i][j]}',end=' ')
        print()
        
def check(x,y,m:list[list[str]]):
    movx = [-1,-1,-1, 0, 0, 1, 1, 1] 
    movy = [-1, 0, 1,-1, 1,-1, 0, 1]
    index = y
    number = ''
    
    while m[x][index].isdigit():
        number += m[x][index]
        index += 1
        if index == len(m[0]):
            break
        
    for k in range(y,index):
        for i in range(len(movy)):
            newx = x + movx[i]
            newy = k + movy[i]
            
            if newx >= 0 and newx < len(m) and newy >= 0 and newy < len(m):
                # print(m[newx][newy])
                if (not m[newx][newy].isdigit()) and (not m[newx][newy] == '.'):
                    return (int(number), True, index - y)
    
    return (int(number), False)
        

txt = txt.replace('\n','')
n = len(text)
text_matrix = [['' for _ in range (n)] for _ in range (n)]

index = 0
for i in range(n):
    for j in range(n): 
            text_matrix[i][j] = txt[index]
            index += 1

valid_tokens = {}

ans = 0
number = ''
for i in range(n):
    skip = 0
    for j in range(n):
        if skip > 0:
            skip -= 1
            continue 
        if text_matrix[i][j].isdigit():
            tuple = check(i,j,text_matrix)
            if tuple[1]:
                print(f'valid number found: {tuple[0]}')
                ans += tuple[0]
                skip = tuple[2]
                
            
              
print(ans)