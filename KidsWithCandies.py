#Get the max of the candies, then loop through the list and find if the extra + candies[i] is more or equal than max
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        most = []
        
        for i in range(len(candies)):
            if(candies[i] + extraCandies >= max_candies):
                most.append(True)
            else:
                most.append(False)
                
        return most
    
    def print_it(self):
        print(self.kidsWithCandies([2,3,5,1,3], 3))

Solution().print_it()