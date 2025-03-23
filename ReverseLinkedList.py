#To reverse the linked list, we swap the direction each node is pointing, so the current node point to 
#the previous and so on.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        
        slow = head
        fast = head
        maxSum = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        nxt = None
        prev = None
        
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        while prev:
            maxSum = max(maxSum, head.val + prev.val)
            prev = prev.next
            head = head.next

        return maxSum
         
         