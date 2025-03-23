#To get the number of euqal rows and column we can make a hash table for each and keep count of the number of times a sequence shows up.
#Then we loop through either the row or column hash table (doesn't matter which) and if a match is found, multiply the counts at that point
#We multiply because if we have multiples then a match can be found more than once. For example in [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
#- (Row 0, Column 0): [3,1,2,2]
#- (Row 2, Column 2): [2,4,2,2]
#- (Row 3, Column 2): [2,4,2,2]
#If we added instead of multiplied, then [2,4,2,2] would be counted 3 times since we have 2 counts in the rows and 1 count in the cols. This is why we must multiply to get the correct answer

class Solution(object):
    def equalPairs(self, grid):
        
        total_cols = {}
        total_rows = {}
        final = 0
        
        
        for i in range(len(grid)):
            #Basically transposes the matrix, probably a function for this
            column = [str(col[i]) for col in grid]
            #Just getting the nested lsits       
            row = [str(row) for row in grid[i]]
            
            #VERY IMPORTANT to concatinate with a seperateor such as a comma, otherwise cases such as [11,1],[1,11] fail becuase it will count it all as 111
            curr_row = (",".join(row))
            curr_col = (",".join(column))
            
            #Getting counts for each, maybe a way to condense this, could put in a function
            if(curr_row in total_rows.keys()):
                total_rows[curr_row] += 1
            else:
                total_rows[curr_row] = 1
                
            if(curr_col in total_cols.keys()):
                total_cols[curr_col] += 1
            else:
                total_cols[curr_col] = 1

        #Loop trhough the rows and if a match is found, multiply the values in the hash map and add it to final
        for i in total_rows:
            if i in total_cols:
                final+=total_cols[i] * total_rows[i]
            
        return final
            
print(Solution().equalPairs([[11,1],
                             [1,11]]))
print(Solution().equalPairs([[13,13],
                            [13,13]]))


print(Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]]))