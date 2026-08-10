# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        Dummy = ListNode(0,head)
        prev = Dummy
        
        for x in range(left - 1):
            prev = prev.next

        curr = prev.next

        for i in range(right - left):
            front = curr.next          
            curr.next = front.next      
            front.next = prev.next     
            prev.next = front

        return Dummy.next
