# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class Solution(object):
    def deleteNode(self, root, key):
        
        if not root:
            return None
        
        if root.val == key:
            # If the key node has both left and right children
            if root.left and root.right:
                # Find the minimum value node in the right subtree
                minimum = self.find_min(root.right)
                root.val = minimum.val  # Replace the value of the current node with minimum
                # Now, delete the minimum node in the right subtree
                root.right = self.deleteNode(root.right, minimum.val)
                
            # If the key node only has a left child
            elif root.left:
                return root.left
            
            # If the key node only has a right child
            elif root.right:
                return root.right
            
            # If the node is a leaf (no children)
            else:
                return None
        
        # Recursively search for the key in the left or right subtree
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root

    def find_min(self, node):
        # Find the node with the minimum value (leftmost node)
        if(node.left == None):
            return node
        else:
            return self.find_min(node.left)