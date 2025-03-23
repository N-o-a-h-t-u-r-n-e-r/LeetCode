#Two pointer solution, i is used to find non zero numbers and i_ptr interates over every number
#The trick is to only iterate i_ptr once a swap is made

class Solution(object):
    def moveZeroes(self, nums):
        
        i_ptr = 0
        
        for i in range(len(nums)):
            
            print(i_ptr, '', i, '' , nums)       
            if(nums[i] != 0):
                nums[i], nums[i_ptr] = nums[i_ptr], nums[i]
                i_ptr+=1
            
            
        print(nums)

Solution().moveZeroes([0,4,2,3,12])