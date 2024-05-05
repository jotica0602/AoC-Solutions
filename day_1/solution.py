from typing import Tuple
import re
import os


class CharNode:
    def __init__(self, value: str, parent: 'CharNode' = None, end_of_string: int = 0, count: int = 1) -> None:
        
        if len(value) > 1:
            print('Invalid node value.')  
        
        else:
            self.value: str = value
            self.childs: list[CharNode] = []
            self.parent = parent
            self.end_of_string: int = end_of_string
            self.count = count

    def __repr__(self) -> str:
        return f'char: {self.value}, childs length: {len(self.childs)}, parent: {self.parent.value}, end of string: {self.end_of_string}, count: {self.count}'

class Trie:
    def __init__(self) -> None:
        self.root = CharNode('')
        
    def prefix_query(self, string_query: str, node: CharNode, index: int = -1, query_kind: int = 1, matched: str = '') -> Tuple[CharNode, int, bool, str]:
        
        '''
        Query Kinds:
        1 - Normal query
        2 - Insert query
        '''
        
        if index + 1 == len(string_query):
            return (node, index, node.end_of_string, matched)
        
        for child in node.childs:
            if child.value == string_query[index + 1]:
                if query_kind == 2:
                    child.count += 1
                    
                matched += child.value
                return self.prefix_query(string_query, child, index + 1, query_kind, matched)
            
        return (node, index, node.end_of_string, matched)
        
    def insert(self, string:str) -> None:
        prefix: Tuple[CharNode, int, bool] = self.prefix_query(string, self.root, query_kind= 2)
        node: CharNode = prefix[0] 
        
        if prefix[2]:
            node.end_of_string += 1
            print(f"Frequency of string: \"{string}\" updated to {node.end_of_string}.")
            return
        
        else:
            for i in range (prefix[1] + 1, len(string)):
                child: CharNode = CharNode(string[i], parent = node)
                node.childs.append(child)
                node = child

            node.end_of_string += 1
            print(f"String: \"{string}\" was inserted.")
        
    def delete(self, string:str) -> None:
        prefix: Tuple[CharNode, int, bool] = self.prefix_query(string, self.root)
        node: CharNode = prefix[0]
        
        # bug when string does not occurs
        if not prefix[2]:
            print(f"String: \"{string}\" does not exists.")
            return
        
        else:
            node.end_of_string -= 1
            
            if node.end_of_string >= 1:
                pass 
            
            else:
                while len(node.childs) == 0 and node.end_of_string == 0:
                    node_index: int = node.parent.childs.index(node)
                    node.parent.childs.pop(node_index)
                    node = node.parent
                    if node.value == '': break
                    
            while node:
                node.count -= 1
                node = node.parent
                
            print(f'String \"{string}\" was deleted.')

trie = Trie()
trie.insert('one')
trie.insert('two')
trie.insert('three')
trie.insert('four')
trie.insert('five')
trie.insert('six')
trie.insert('seven')
trie.insert('eight')
trie.insert('nine')

lines = []

with open('Desktop/AoC/Trebuchet/input2.txt', 'r') as file:
    text = file.read()
    lines = text.split()

ans = 0


### Part one
# for line in lines:
#     num = []
#     for char in line:
#         if char.isdigit():
#             num.append(char)
#     number = int(num[0]+num[len(num)-1])
#     ans += number
# print(ans)        


### Part two
for line in lines:
        num = []
        index = 0
        
        while index < len(line):
            if line[index].isdigit():
                num.append(line[index])
                index += 1
            else:
                numstr = ''
                
                while index < len(line) and not line[index].isdigit(): 
                    numstr += line[index]
                    index += 1
                    
                while len(numstr) != 0:
                    prefix = trie.prefix_query(numstr,trie.root)
                    if prefix[2] > 0:
                        if prefix[3] == 'one':
                            num.append('1')
                        elif prefix[3] == 'two':
                            num.append('2')
                        elif prefix[3] == 'three':
                            num.append('3')
                        elif prefix[3] == 'four':
                            num.append('4')
                        elif prefix[3] == 'five':
                            num.append('5')
                        elif prefix[3] == 'six':
                            num.append('6')
                        elif prefix[3] == 'seven':
                            num.append('7')
                        elif prefix[3] == 'eight':
                            num.append('8')
                        elif prefix[3] == 'nine':
                            num.append('9')
                            
                        numstr = numstr[prefix[1]:]
                    else:
                        numstr = numstr[1:]

        # print(num[0]+num[len(num)-1])
        number = int(num[0]+num[len(num)-1])
        ans += number

print(ans) 