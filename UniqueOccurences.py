#Use a hash map (dictonary) to store the array value as the key and the count as the value in the dictionary
#Then convert to a set (which only holds unique values) and check if the lengths are equal. If not then
#We have duplicates

class Solution(object):
    def uniqueOccurrences(self, arr):
        hash_map = {}
        
        for n in arr:
            
            if n in hash_map.keys():
                hash_map[n] += 1
            else:
                hash_map[n] = 1
            
        arr1 = list(hash_map.values())
        arr2 = list(set(arr1))
        
        if len(arr1) == len(arr2):
            return True
        
        return False
    
print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
        