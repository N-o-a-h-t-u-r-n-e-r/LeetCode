#A tricky one using DFS to find the lowest common ancestor, lowest being height-wise not value.
#Solution is to define a l and r variable to check left and right subtrees for p or q.
#If p or q is found then return it up the tree until either both are found or only 1 is present


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        
        #Base case to find p and q
        if(root == None or root == p or root == q):
            return root
        
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        
        #If both are found at this level, return the current root, also works if l or r IS the root
        if(l and r):
            return root
        
        #If we have only found l at this level, then return it up the call stack
        if(l and not r):
            return l
        
        #If we have only found r at this level, then return it up the call stack
        if(r and not l):
            return r
        