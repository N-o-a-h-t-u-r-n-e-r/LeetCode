#Trick is using a stack to act like a form of recursion
#Loop through and add the found letters to the stack, followed by the number
#Once a ']' is found, we pop from our stack and add the current string to the previous one in the stack


class Solution(object):
    def decodeString(self, s):
        
        #curr_string as a list since it saves time
        stack = []; curr_num = 0; curr_string = []
        for c in s:
            
            #If a left bracket is found, then add the current string and number to the stack and reset them
            if c == '[':
                stack.append(curr_string)
                stack.append(curr_num)
                curr_string = []
                curr_num = 0
            #If a right bracket is found, then we start popping from our stack, this ensures that nested
            #brackets are handled in the correct order. Its important we put the previous string first
            elif c == ']':
                num = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + num*curr_string
            #Calculation to handle cases where the number is double digits or more
            elif c.isdigit():
                curr_num = curr_num*10 + int(c)
            #Finding our temporary current string
            else:
                curr_string.append(c)
            
        return ''.join(curr_string)
    
print(Solution().decodeString("3[a2[c]]"))