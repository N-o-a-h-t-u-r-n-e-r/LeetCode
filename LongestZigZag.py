# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root, left=0, right=0):
        maxLen = max(left, right)

        if root.left:
            maxLen = max(maxLen, self.longestZigZag(root.left, right + 1, 0)) 
        if root.right:
            maxLen = max(maxLen, self.longestZigZag(root.right, 0, left + 1))  

        print(maxLen, left, right)
        return maxLen