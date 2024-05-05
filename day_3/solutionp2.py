with open('input1.txt') as file:
    text = file.readlines()
    
with open('input1.txt') as file: 
    txt = file.read()

class MyDictionary:
    def __init__(self) -> None:
        self.list = []
    
    def add(self, tuple):
        for i in range(len(self.list)):
            if self.list[i][0] == tuple[0] and self.list[i][1] == tuple[1]:
                self.list[i] = (self.list[i][0], self.list[i][1], self.list[i][2] + 1, self.list[i][3]) 
                self.list[i][3].append(tuple[3][0])
                return

        self.list.append(tuple)

def print_matrix(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            print(f'{m[i][j]}',end=' ')
        print()
        
def check(x,y,m:list[list[str]],dictionary:MyDictionary):
    movx = [-1,-1,-1, 0, 0, 1, 1, 1] 
    movy = [-1, 0, 1,-1, 1,-1, 0, 1]
    index = y
    number = ''
    
    while m[x][index].isdigit():
        number += m[x][index]
        index += 1
        if index == len(m[0]):
            break
        
    mask = [[False for _ in range(len(m))] for _ in range(len(m))]
        
    for k in range(y,index):
        for i in range(len(movy)):
            newx = x + movx[i]
            newy = k + movy[i]
            if newx >= 0 and newx < len(m) and newy >= 0 and newy < len(m):
                # print(m[newx][newy])
                if m[newx][newy] == '*' and not mask[newx][newy]:
                    dictionary.add((newx,newy,1,[int(number)]))
                    mask[newx][newy] = True
                    
    
    return index - y

txt = txt.replace('\n','')
n = len(text)
text_matrix = [['' for _ in range (n)] for _ in range (n)]

index = 0
for i in range(n):
    for j in range(n): 
            text_matrix[i][j] = txt[index]
            index += 1

ans = 0
my_dictionary = MyDictionary()
number = ''
for i in range(n):
    skip = 0
    for j in range(n):
        if skip > 0:
            skip -= 1
            continue 
        if text_matrix[i][j].isdigit():
            skip = check(i,j,text_matrix,my_dictionary)
            

for element in my_dictionary.list:
    if element[2] == 2:
        k = element[3][0] * element[3][1]
        ans += k
                      
print(ans)