import re
        
with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

pattern = r'\w+'
graph = {}

for i in range(2,len(lines)):
    node_values = re.findall(pattern,lines[i])
    node = node_values.pop(0)
    graph[node] = []
    for node_value in node_values:
        graph[node].append(node_value)

directions = lines[0]
index = 0
current_node = 'AAA'
ans = 0

while True:
    
    if directions[index] == 'L':
        current_node = graph[current_node][0]
        
    elif directions[index] == 'R':
        current_node = graph[current_node][1]
    
    ans += 1
    index +=1         
    
    if index == len(directions):
        index = 0
        
    if current_node == 'ZZZ':
        break

print(ans)