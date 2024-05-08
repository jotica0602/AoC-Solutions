import re
import sys
import time


class AVLNode(object):
    def __init__(self,value:tuple[int,int,int]):           
        self.height = 1
        self.size = 1
        self.left = None
        self.end = value[1] + value[2] - 1
        self.value = value[1]
        self.start = value[0]
        self.right = None
    
    def f(self, seed:int):
        return seed - self.value + self.start
        
    def __str__(self) -> str:
        return str(self.value)

class AVLTree: 
    def __init__(self, root: AVLNode = None) -> None:
        self.root = root
        
    def find(self,root:AVLNode,key:int):
        if not root:
            return key
        if key < root.value:
            return self.find(root.left,key)
        if key >= root.value and key <= root.end:
            return root.f(key)
        else:
            return self.find(root.right,key)
    
    def traverse(self,root:AVLNode, list:list):
        # leaf node
        if not root.left and not root.right:
            list.append(root.value)
            return list
        
        # dfs left node
        if root.left:
            self.traverse(root.left,list)
        
        list.append(root.value)
    
        #dfs right node
        if root.right:
            self.traverse(root.right,list)
        return list
    
    def get_balances(self,root:AVLNode, list:list):
        if not root.left and not root.right:
            list.append(self.get_balance(root))
            return list
        if root.left:
            self.get_balances(root.left,list)
        list.append(self.get_balance(root))
        if root.right:
            self.get_balances(root.right,list)
        return list
    
    def print_balance(self,root:AVLNode):
        list = []
        print("node balances:")
        print(self.get_balances(root,list))
        
    def print_tree(self):
        list = []
        print("tree items:")
        print(self.traverse(self.root,list))
    
    def rank(self,root:AVLNode,key):
        if root is None: return 0
        if root.value < key: return 1 + self.rank(root.left,key) + self.rank(root.right,key)
        else: return self.rank(root.left,key)

    def predecessor(self,node:AVLNode):
        if not node.right: return node
        return self.predecessor(node.right)
    
    def successor(self, node:AVLNode):
        if not node.left: return node
        return self.successor(node.left)
    
    def get_height(self,node:AVLNode):
        if not node: return 0
        return node.height

    def get_balance(self,node:AVLNode):
        if not node:
            return -1
        return self.get_height(node.right) - self.get_height(node.left)
            
    def update_height(self,node:AVLNode):
        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))
        
    def left_rotate(self,x:AVLNode):
    #     x                                 y
    #    /  \                             /   \ 
    #   T1   y     Left Rotate (x)       x      z
    #       /  \   - - - - - - - ->     / \    / \
    #      T2   z                      T1  T2 T3  T4
    #          / \
    #         T3  T4
    
        y = x.right                                         
        t2 = y.left                         
        x.right = t2
        y.left = x        
        self.update_height(x)
        self.update_height(y)
        return y
    
    def right_rotate(self,x:AVLNode):
    #
    #          x                                      y 
    #         / \                                   /   \
    #        y   T4      Right Rotate (x)          z      x
    #       / \          - - - - - - - - ->      /  \    /  \ 
    #      z   T3                               T1  T2  T3  T4
    #     / \
    #   T1   T2
        
        y = x.left
        t3 = y.right
        x.left = t3
        y.right = x
        self.update_height(x)
        self.update_height(y)
        return y
    
    def balance(self,root:AVLNode,key):
        # Update Height
        self.update_height(root)
        
        # Get Balance
        root_balance = self.get_balance(root)
        left_balance = self.get_balance(root.left)
        right_balance = self.get_balance(root.right)
        
        # Handle Cases
        # (++,+)
        if root_balance == 2 and right_balance == 1:
            return self.left_rotate(root)
        # (++,-)
        if root_balance == 2 and right_balance == -1:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        # (--,-)
        if root_balance == -2 and left_balance == -1:
            return self.right_rotate(root)
        # (--,+)
        if root_balance == -2 and left_balance == 1:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
            
        return root
            
    def insert(self, key, ranges, root:AVLNode):
        if not self.root:
            self.root = AVLNode(ranges)
            root = self.root
        elif not root:
            root = AVLNode(ranges)
            return root   
        elif key < root.value:
            root.left = self.insert(key,ranges,root.left)
        elif key > root.value:
            root.right = self.insert(key,ranges,root.right)
        else:
            return root
        
        return self.balance(root,key)
    
    def remove(self,root:AVLNode,key):
        if not root:
            return root
        elif key < root.value:
            root.left = self.remove(root.left,key)
        elif key > root.value:
            root.right = self.remove(root.right,key)
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is not None and root.right is None:
                return root.left
            if root.left is None and root.right is not None:
                return root.right
            else:
                succesor = self.successor(root.right)
                temp = root.value
                root.value = succesor.value
                succesor.value = temp
                root.right = self.remove(root.right,temp)
        
        # Update Height
        self.update_height(root)
        root_balance = self.get_balance(root)
        left_balance = self.get_balance(root.left)
        right_balance = self.get_balance(root.right)
        
        # Handle Cases
        # (++,+) | (++,.)
        if (root_balance == 2) and (right_balance >= 0):
            return self.left_rotate(root)
        # (--,-) | (--,.)
        if (root_balance == -2) and (right_balance <= 0):
            return self.right_rotate(root)
        # (++,-)
        if (root_balance == 2) and (left_balance == -1):
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        # (--,+)
        if (root_balance == -2) and (right_balance == 1):
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        return root

tree = AVLTree()

with open('input.txt') as file:
    text = file.read()
    lines = text.split(sep='\n')

pattern = r'\d+'
seeds = [int(x) for x in re.findall(pattern,lines[0])]
result = sys.maxsize

def map(x,a,b,c) -> tuple[int,bool]:
    if x < b or x > b + c - 1: 
        return (x, False)
    else: 
        return (x - b + a, True)

counter = -1

seed_to_soil = AVLTree()
soil_to_fertilizer = AVLTree()
fertilizer_to_water = AVLTree()
water_to_light = AVLTree()
light_to_temperature = AVLTree()
temperature_to_humidity = AVLTree()
humidity_to_location = AVLTree()
avl_list = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

lines = lines[1:]
for line in lines:
    if line == '':
        continue
    elif not line[0].isdigit():    
        counter += 1
    else:
        ranges = [int(x) for x in re.findall(pattern,line)]
        avl_list[counter].root = avl_list[counter].insert(ranges[1],ranges,avl_list[counter].root)
        
print('done inserting')

for i in range(0,len(seeds)-1,2):
    for j in range(seeds[i],seeds[i] + seeds[i+1]+1):
        seed = j
        for k in range(len(avl_list)):
            seed = avl_list[k].find(avl_list[k].root, seed)
        result = min(result,seed)

print(f'result: {result}')
print('end')
