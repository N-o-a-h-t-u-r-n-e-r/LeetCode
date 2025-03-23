#Sliding window technique is used. A window of size k is created and then slid through the array, finding the 
#max amount of vowels in the window

class Solution(object):
    def maxVowels(self, s, k):
        
        vowels = ['a','e','i','o','u']
        max_vowels = 0
        num_vowels = 0
        
        #Used to start the window from 0 to k
        for i in range(0,k):
          if(s[i] in vowels):
              num_vowels+=1
        
        #Incase we have a single char vowel
        max_vowels = num_vowels
        
        for i in range(len(s) - k):      
             
            #If the char leaving the window is a vowel, subtract from our count   
            if(s[i] in vowels):
                num_vowels-=1
            #If the char entering the window is a vowel, add to our count
            if(s[i+k] in vowels):
                num_vowels+=1
            
            #Get the new max, if there is one    
            max_vowels = max(max_vowels,num_vowels)
                    
        return max_vowels
    
print(Solution().maxVowels("weallloveyou", 7))
        