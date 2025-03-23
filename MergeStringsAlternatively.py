def mergeAlternately(word1, word2):
    l1 = len(word1)
    l2 = len(word2)
    
    n = min(l1,l2)
    lst = []
    for i in range(n):
        lst.append(word1[i])
        lst.append(word2[i])
        
    
    if(l1 > l2):
        lst.append(word1[l2:])
        
        
    if(l2 > l1):
        lst.append(word2[l1:])
                
    s = "".join(lst)
    return s


print(mergeAlternately("abcd", "pq"))