# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        
        #Base Case
        if head == None or head.next == None: 
            return head 
        
        #Odd and even are dummy head nodes, and pointers to traverse it.
        odd = ListNode(0) 
        odd_ptr = odd
        even = ListNode(0)
        even_ptr = even 
        #Keep track of currrent index
        idx = 1 
        
        while head != None :
            if idx % 2 == 0:
                #Set the pointer to the current value and move to that node
                even_ptr.next = head
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            #Move to next node
            head = head.next
            idx+=1
            
        #Make sure the end of the even pointer isnt pointing to garbage memory and conncect the two lists.
        #Its odd.next and even.next since the first nodes are garbage
        even_ptr.next = None
        odd_ptr.next = even.next
        return odd.next