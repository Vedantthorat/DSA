# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            # Check if there are k nodes remaining
            kth = prev_group_end
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_start = prev_group_end.next
            next_group_start = kth.next
            
            # Reverse k nodes
            prev = next_group_start
            curr = group_start
            
            while curr != next_group_start:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Connect reversed group
            prev_group_end.next = kth
            prev_group_end = group_start
