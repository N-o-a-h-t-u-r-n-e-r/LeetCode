#Since its a binary search tree its easy to find the target value by moving left or right

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        
        if(not root):
            return
        
        if (root.val == val):
            return root
    
        #Go left if current value is greater than target value, otherwise go right.
        if(root.val > val):
           return self.searchBST(root.left, val)
        else:
           return self.searchBST(root.right, val)
        