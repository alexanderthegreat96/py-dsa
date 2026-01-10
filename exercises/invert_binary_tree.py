# Binary tree: 
#     4
#    / \
#   2   7
#  / \ / \
# 1  3 6  9

# Inverted binary tree:
#     4
#    / \
#   7   2
#  / \ / \
# 9  6 3  1

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val : int=0, left : Optional[TreeNode]= None, right: Optional[TreeNode]=None):
        self.val = val
        self.left = left
        self.right = right
    
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # set the left child to the right child and vice versa 
        root.left, root.right = root.right, root.left
        
        # call the function recursively on both children
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root

def invert_tree_iterative(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    # We use deque for O(1) pops from the left
    queue = deque([root])
    
    while queue:
        # 1. Take the current node out
        current = queue.popleft()
        
        # 2. Perform the swap
        current.left, current.right = current.right, current.left
        
        # 3. Add children to the queue to be processed later
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
            
    return root