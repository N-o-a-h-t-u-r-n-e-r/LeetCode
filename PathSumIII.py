#This one is tricky as it requires nested recursion to cover all nodes. (Can get around this using hashmaps but didnt do)
#To check every path, we use the dfs function to search the whole tree, and then the main pathSum function to search the
#new node with a 0 starting sum (basically making it the new root)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    #Global counter
    def __init__(self):
        self.total = 0 
    
    #Main dfs function
    def dfs(self, node, sum, targetSum):
            #Return 0 in case of empty input
            if(not node):
                return 0
            
            #Add new sum and check if target sum is found
            sum += node.val
            if(sum == targetSum):
                self.total += 1
                
            #Recursivly run the left and right node with the new sum
            self.dfs(node.left, sum, targetSum)
            self.dfs(node.right, sum, targetSum)
            
            
    
    def pathSum(self, root, targetSum):
        if(not root):
            return 0

        #Start the dfs recurrsion
        self.dfs(root, 0, targetSum)
        #Nested recursion that makes sure each node is being used as a root
        self.pathSum(root.right, targetSum)
        self.pathSum(root.left, targetSum)
        
        return self.total
            
            
            
            
            
        