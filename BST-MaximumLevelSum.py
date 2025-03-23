#Just have to get the right most node at the current level

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        if not root:
            return 0

        queue = []
        result = root.val 
        level = 0
        ans = 1
        queue.append(root)
        while(queue):
            curr_len = len(queue)
            total = 0 
            #Traverse in a BFS manner (Explore current level)
            for i in range(curr_len):
                curr = queue.pop(0)
                total += curr.val
                
                
                if curr.left:
                    queue.append(curr.left)               
                if curr.right:
                    queue.append(curr.right)
            level+=1
            if(total > result):
                result = total
                ans = level
                    
                    
        return ans