# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head_pt = head
        curr = head.next
        head_pt.next = None
        while curr.next:
            #5
            temp = curr.next
            #4.next = 3
            curr.next = head_pt
            #3 becomes 4
            head_pt = curr
            #4 becomes 5
            curr = temp
        curr.next = head_pt
        return curr
        