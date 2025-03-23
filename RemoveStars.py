#Very easy to remove the stars and the letter to the left from the string, simply iterate 
#through the string and if a star is found
#then we pop from our stack, otherwise we will push the current letter onto the stack. This method
#ensures we always are removing the letter to the left of the star

class Solution(object):
    def removeStars(self, s):
       
       #In python, we can use a list as a stack
        stack = []
        
        for l in s:
            if l == '*':
                stack.pop()
            else:
                stack.append(l)
             
        #Join the result   
        return "".join(stack)
    
print(Solution().removeStars("leet**cod*e"))
        