#Trick is to break down operation1 and operation2 into what they really mean.
#For operation1, since we can freely swap any two letters, then as long as each string has the same letters
#operation1 is accounted for. For operation two, we need to check the frequency of the letters.
#If both strings have the same count of unique letters, then the string is "close"


class Solution(object):
    def closeStrings(self, word1, word2):
        
        #Hash maps to keep track of letter frequencies
        letters1 = {}
        letters2 = {}
        
        
        #If the lengths aren't the same, then obviously its false
        if len(word1) != len(word2):
            return False
        
        #This checks to make sure they only have the same letters
        if set(word1) != set(word2):
            return False
        
        #Iterate through both words, making a frequency count of each letter in the hashmap
        for n, k in zip(word1, word2):
            if n in letters1.keys():
                letters1[n] +=1
            else:
                letters1[n] = 1
                
            if k in letters2.keys():
                letters2[k] +=1
            else:
                letters2[k] = 1
               
        #Sort the frequencies and if they are the same, then the strings are valid. If the frequencies are 
        #different that means we cannot use operation2 to make the strings the same. 
        list1 = sorted(letters1.values())
        list2 = sorted(letters2.values())
        
        if(list1 != list2):
            return False
        
        return True
    
print(Solution().closeStrings("ababbzc", "babzzcz"))