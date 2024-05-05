import re
class AVLNode(object):
    def __init__(self,value):           
        self.height = 1
        self.size = 1
        self.left = None
        self.value = value
        self.right = None
        
    def __str__(self) -> str:
        return str(self.value)

class AVLTree: 
    def find(self,root:AVLNode,key:int):
        if not root: 
            return None
        if key < root.value and root.left:
            return self.find(root.left, key)
        if key > root.value and root.right:
            return self.find(root.right, key)
        return root
    
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
        
    def print_tree(self,root):
        list = []
        print("tree items:")
        print(self.traverse(root,list))
    
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
            
    def insert(self,root:AVLNode,key):
        if not root:
            return AVLNode(key)
        elif key < root.value:
            root.left = self.insert(root.left,key)
        else:
            root.right = self.insert(root.right,key)
        
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
root = None

with open('input.txt') as file:
    text = file.read()

pattern = r'Card +\w+:(( +\d+)+) +\|(( +\d+)+)+'    
matches = re.findall(pattern,text)
ans = 0
for match in matches:
    root = None
    number = ''
    numbers = match[0] + ' '
    index = 0
    while index < len(numbers):
        if numbers[index].isdigit():
            number += numbers[index]
            
        else: 
            if number != '':
                root = tree.insert(root,int(number))
            number = ''
        index += 1
    
    numbers = match[2] + ' '
    index = 0
    cardvalue = 0
    while index < len(numbers):
        if numbers[index].isdigit():
            number += numbers[index]
            
        else: 
            if number != '':
                node = tree.find(root, int(number))
                if node.value == int(number):
                    if cardvalue == 0:
                        cardvalue = 1
                    else:
                        cardvalue = 2 * cardvalue
            number = ''
        index += 1
    ans += cardvalue

print(ans) 
b:list = []
print('end')