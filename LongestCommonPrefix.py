def longestPre(v):
    final = ''
    v = sorted(v)
    begin = v[0]
    last = v[-1]
        
    for i in range(min(len(begin), len(last))):
        if(begin[i] != last[i]):
            return final
        final += begin[i]
       
    return final
            
    
    
strs = ["flower","flow","flight"]
print(longestPre(strs))