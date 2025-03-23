#The trick is to only check on 0s, by doing this we only have to check the one spot ahead and not behine
#since there cannot be two or more 1s in a row

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        length = len(flowerbed)
        i = 0
        
        #While loop instead of for so we can jump multiple spots with i
        #Loop until i = length or n is 0
        while i < length and n > 0:
            #If current index is 1, skip ahead 2 to check next valid spot
            if flowerbed[i] == 1:
                i += 2 
            #Check if at the last spot in the array or if the next spot is 0, if so then plant 
            elif i == length - 1 or flowerbed[i + 1] == 0:            
                n -= 1
                i += 2
            #Reaching here means the next spot is a 1, so skip 3   
            else:
                i += 3  
        return n <= 0 
        
        
flower = Solution()
print(flower.canPlaceFlowers([1,0,0,0,1,0,0], 1))