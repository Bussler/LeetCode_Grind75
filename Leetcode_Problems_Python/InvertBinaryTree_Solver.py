from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# M: create Tree from list
def create_tree_from_list(in_list: List[int]) -> TreeNode:
    if not in_list:
        return None
    
    root = TreeNode(in_list[0])
    queue = [root]
    i = 1
    
    while queue:
        node = queue.pop(0)
        if i < len(in_list) and in_list[i] is not None:
            node.left = TreeNode(in_list[i])
            queue.append(node.left)
        i += 1
        if i < len(in_list) and in_list[i] is not None:
            node.right = TreeNode(in_list[i])
            queue.append(node.right)
        i += 1
    
    return root

# M: print Tree structure
def printTree(root):
    if not root:
        return
    
    levels = []
    current_level = [root]
    
    while not all(elem is None for elem in current_level):
        levels.append(current_level)
        next_level = []
        for node in current_level:

            if node is None:
                next_level.append(None)
                continue

            next_level.append(node.left)
            next_level.append(node.right)

        current_level = next_level
    
    height = len(levels)
    width = 2**(height-1)*3-1
    
    for i, level in enumerate(levels):
        level_str = ''
        between_node_space = ' ' * (2**(height-i-1)*3-3)
        level_str += between_node_space
        for node in level:
            if node:
                node_val_str = str(node.val).center(3, ' ')
                level_str += node_val_str + between_node_space
            else:
                level_str += ' ' * 6 + between_node_space
        print(level_str.center(width, ' '))



class InvertBinaryTree_Sovler(Solver):

    def solve(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current_level = [root]

        while not all(elem is None for elem in current_level):
            next_level = []
            for node in current_level:
                if node is None:
                    next_level.append(None)
                    continue
                
                # M: change l/r nodes for each level!
                node.left, node.right = node.right, node.left
                
                current_level.append(node.left)
                current_level.append(node.right)
            
            current_level = next_level

        return root    


    def test_solve(self):
        root_list = [4,2,7,1,3,6,9]
        root_node = create_tree_from_list(root_list)

        print("Orig_Tree:")
        printTree(root_node)

        inverted = self.solve(root_node)
        print("Inverted: ")
        printTree(inverted)
