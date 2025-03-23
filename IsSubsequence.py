#Trick is to loop through and have a pointer for s that only increments once a match is found
#If k equals the length of string s, then a substring has been found

class Solution(object):
    def isSubsequence(self, s, t):
        
        if(s == ""):
            return True
        
        k = 0
        for i in range(len(t)):
            if(t[i] == s[k]):
                k+=1
            if(k == len(s)):
                return True
        
        return False
        
