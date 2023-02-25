# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # #using hash set
        # if not head:
        #     return False
        # visit = set()
        # while head.next:
        #     if head in visit:
        #         return True
        #     visit.add(head)
        #     head = head.next
        # return False
            
        #tortoise and hare method: O(1) memory
        # if not head:
        #     return False
        # slow, fast = head, head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False
        
#---------- revisit ---------
        
        # #O(n) memory
        # if not head:
        #     return False
        # seen = set()
        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next
        # return False
        
        #O(1) memory: Tortoise and hare:
        if not head:
            return False
        pslow, pfast = head, head
        while pfast is not None and pfast.next is not None:
            pslow = pslow.next
            pfast = pfast.next.next
            if pslow == pfast:
                return True
        return False
        
            
        
            
            
        