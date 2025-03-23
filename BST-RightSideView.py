#Just have to get the right most node at the current level

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        queue = []
        result = []
        queue.append(root)
        while(queue):
            curr_len = len(queue)
            
            #Traverse in a BFS manner (Explore current level)
            for i in range(curr_len):
                curr = queue.pop(0)
                
                #Gets the last added value to the queue (rightmost at that level)
                if i == curr_len - 1:
                  result.append(curr.val)  
                  
                
                if curr.left:
                    queue.append(curr.left)               
                if curr.right:
                    queue.append(curr.right)
                    
                    
        return result