#Trick is to convert lists num1 and num2 to sets, which don't allow duplicates
#Then check for integers not in the other set, and append to answers

class Solution(object):
    def findDifference(self, nums1, nums2):
        
        
        answers = [[],[]]
        #Convert to sets
        set1 = set(nums1)
        set2 = set(nums2)
        
        #Find elements not in the other set 
        for n in set1:
            if n not in set2:
                answers[0].append(n)
                
        for n in set2:
            if n not in set1:
                answers[1].append(n)
                
        
        return(answers)
            
    
    
print(Solution().findDifference([1,2,3,3], [1,1,2,2]))
        