# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        to_reveret = head
        

        while to_reveret:
            front = to_reveret.next
            to_reveret.next = prev
            prev = to_reveret
            to_reveret = front

        head = prev
        return head