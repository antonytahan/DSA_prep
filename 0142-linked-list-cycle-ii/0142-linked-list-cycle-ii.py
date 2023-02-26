# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer1, pointer2 = head, head
        cycleCount = self.cycleCount(head)
        if cycleCount is 0:
            return None
        print(cycleCount)
        for i in range(cycleCount):
            pointer2 = pointer2.next
        while pointer2 is not None and pointer2.next is not None:
            if pointer1 == pointer2:
                return pointer2
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return None
            
        
    def cycleCount(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        count = 0
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return self.calcCycleLength(slow)
        return 0
            
    def calcCycleLength(self, pointer: int) -> int:
        count = 0
        curr = pointer
        while True:
            curr = curr.next
            count += 1
            if curr == pointer:
                break
        return count
        
        