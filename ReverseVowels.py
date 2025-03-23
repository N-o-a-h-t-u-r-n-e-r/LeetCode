#Trick is to have two pointers, one starting at the end and one at the beginning. 
#Move them towards each other until both find a vowel, then swap those vowels

class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        # Convert the string into a list
        final = list(s)
        
        # Initialize two pointers: one at the start and one at the end
        left = 0
        right = len(final) - 1
        
        while left < right:
            # Move the left pointer to the next vowel
            if final[left] not in vowels:
                left += 1
                continue
            
            # Move the right pointer to the previous vowel
            if final[right] not in vowels:
                right -= 1
                continue
            
            # Swap the vowels
            final[left], final[right] = final[right], final[left]
            left += 1
            right -= 1
        
        
        return ''.join(final)