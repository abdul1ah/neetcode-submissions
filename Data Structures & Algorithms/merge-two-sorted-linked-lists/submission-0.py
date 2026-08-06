# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = list1
        curr2 = list2
        
        Merged = ListNode(0)
        tail = Merged

        while curr1 and curr2:

            front1 = curr1.next
            front2 = curr2.next

            if curr1.val == curr2.val:
                tail.next = curr1
                tail = curr1
                tail.next = curr2
                tail = curr2
            
                curr1 = front1
                curr2 = front2


            elif curr1.val < curr2.val:
                tail.next = curr1
                tail = curr1
                curr1 = front1 
            
            else: 
                tail.next = curr2
                tail = curr2
                curr2 = front2

        if not curr1:
            tail.next = curr2

        if not curr2:
            tail.next = curr1

        return Merged.next

        