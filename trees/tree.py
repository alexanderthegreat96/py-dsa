# tree structures
# This module defines a binary tree node and provides methods to invert a binary tree

# Binary tree:
# every element is greater than the left child but smaller than the right child (in a BST)
# it's a recursive data structure where each node has at most two children
# big O(log n) for balanced trees for search, insert, delete

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val: int) -> None:
        """Inserts a new value into the binary search tree."""
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
        
    def delete(self, val: int) -> Optional['TreeNode']:
        """Deletes a value from the binary search tree and returns the new root."""
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
        else:
            # Node with only one child or no child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            
            # Copy the inorder successor's value to this node
            self.val = min_larger_node.val
            
            # Delete the inorder successor
            self.right = self.right.delete(min_larger_node.val)
        
        return self
    
    def invert(self) -> Optional['TreeNode']:
        """Inverts the binary tree rooted at this node."""
        if not self:
            return None
        
        # Swap the left and right children
        self.left, self.right = self.right, self.left
        
        # Recursively invert the left and right subtrees
        if self.left:
            self.left.invert()
        if self.right:
            self.right.invert()
        
        return self
    
def search_tree(root: Optional[TreeNode], val: int) -> bool:
    """Searches for a value in the binary search tree."""
    if root is None:
        return False
    # check current node
    if val == root.val:
        return True
    
    # search left or right subtree
    elif val < root.val:
        return search_tree(root.left, val)
    else:
        return search_tree(root.right, val)