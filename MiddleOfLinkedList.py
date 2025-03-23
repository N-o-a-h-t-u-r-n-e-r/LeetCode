#Trick is to use a slow and a fast pointer, the fast pointer moves twice as fast as the slow pointer, which moves 1 node at a time.
#By doing this until fast == None or fast.next == None, we end up with the slow pointer pointing to the middle.


class Solution(object):
    def deleteMiddle(self, head):
        if not head.next:
            return None
        
        prev = None
        slow = head
        fast = head
        
        while(fast != None and fast.next != None):
            prev = slow
            slow = slow.next
            #Move it two spaces
            fast = fast.next.next
          
        #Linking the previous to the next, which removes the middle  
        prev.next = slow.next
        return head
        