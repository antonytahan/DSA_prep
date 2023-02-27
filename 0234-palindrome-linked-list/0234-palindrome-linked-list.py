# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        curr2 = head
        middle = self.findMiddle(head)
        swap_node = middle.next
        middle.next = None
        
        while swap_node:
            swap_node_next = swap_node.next
            swap_node.next = middle
            middle = swap_node
            swap_node = swap_node_next

        while middle:
            if middle.val != curr.val:
                return False
            middle = middle.next
            curr = curr.next
        return True
        
        
    
    def findMiddle(self, head : Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        