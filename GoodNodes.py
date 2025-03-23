#Just need to use DFS to traverse the tree, keeping track of the max value of each subtree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def getMax(root1, maxNum, count):
            
            if(not root1):
                return 
            
            
            if(root1.val >= maxNum):
                maxNum = root1.val
                count[0] += 1
            
            getMax(root1.left, maxNum, count)
            getMax(root1.right, maxNum, count)
                
       
          
        #Use a list for the count variable since lists are mutable, unlike integers which are immutable and 
        #Would be passed by value instead of by reference like we need.  
        count = [0]  
        getMax(root, root.val, count)
        return count[0]