#Trick is a two pointer solution, one starting at the left and one starting at the right
#Only move the pointer that is currently pointing to the lower value, and at each step
#Calculate the total area

class Solution(object):
    def maxArea(self, height):
        
        right = len(height)-1
        left = 0
        
        width = len(height)-1
        area = 0
              
        while(left < right):
            
            new_area = min(height[left], height[right]) * width
            if(new_area > area):
                area = new_area
                
            
            if(height[left] >= height[right]):
                right-=1
                width-=1
                continue
            
            if(height[right] > height[left]):
                left+=1
                width-=1
                continue
            
        return area
    

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
                
        
        