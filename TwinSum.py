


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        
        maxSum = 0
    
        slow = head
        fast = head.next
        
        nxt = None
        prev = None
        nxtHead = None
        
        while(fast.next):
            nxtHead = slow.next
            nxt = slow.next
            slow.next = prev
            prev = slow          
            slow = nxt
            fast = fast.next.next
            
            
            
        while(nxtHead):
            maxSum = max(maxSum, head.val + nxtHead.val)
            head = head.next
            nxtHead = nxtHead.next
            
        return maxSum
        
        
        