#Solution is to check if they are euqal when added same forwards and back, and if so, slice them alternatingly until they are the same string.

def gcdOfStrings(str1, str2):
    
    #If the strings arent the same when concatenated forward and backward, there is no GCD.
    if((str1 + str2) != (str2 + str1)):
        return ""

    #If the above check is true and they are the same length, then they are the same string so return either one.
    if(len(str1) == len(str2)):
        return str1
    
    #If str1 is bigger, then "substract" str2 fromm it
    if len(str1) > len(str2):
        print(str1, " ", str2)
        return gcdOfStrings(str1[len(str2):], str2)
     
    #Same as above but if str2 is bigger this pass 
    print(str1, " ", str2)
    return gcdOfStrings(str1, str2[len(str1):])
    

print(gcdOfStrings("ABABAB", "ABAB"))