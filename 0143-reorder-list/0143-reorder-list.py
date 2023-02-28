# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
#         #finding half of LL:
#         slow, fast = head, head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
            
#         #reversing second half:
#         prev = None
#         curr = slow.next
#         #need this line below for when we start merging the two lists
#         #the None here is what created the separation of the two lists, otherwise it is still one LL just with the second half of the elements reversed
#         slow.next = None
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
        
#         #merging the two LLs:
#         #curr is now the head of the second half
#         first_p, second_p = head, prev
#         while second_p:
#             temp1, temp2 = first_p.next, second_p.next
#             first_p.next = second_p
#             second_p.next = temp1
#             second_p = temp2
#             first_p = temp1


##Stack Solution:
#         stack = []
#         cur = head
#         end = head
#         while cur:
#             stack.append(cur)
#             cur = cur.next
        
#         for i in range(len(stack)//2):
#             #print(head)
#             nxt = head.next
#             node = stack.pop()
#             head.next = node
#             head = head.next
#             head.next = nxt
#             head = head.next
#             #print(head)
            
#         if head != None:
#             head.next = None
            
        
        
        #Deque approach:
#         #shitty solution though, don't use
#         lst = deque([])
#         cur = head
#         while cur:
#             lst.append(cur)
#             cur = cur.next
        
#         for i in range(len(lst)//2):
#             first = lst.popleft()
#             last = lst.pop()
#             nxt = first.next
#             first.next = last
#             if last == first.next and len(lst) == 0:
#                 last.next = None
#             else:
#                 last.next = nxt
#         if lst:
#             node = lst.pop()
#             node.next = None



#---------revisit --------------
#         if not head:
#             return None
        
#         tail = head
#         nodes = []
        
#         while tail:
#             nodes.append(tail)
#             tail = tail.next
            
#         l, r = 0, len(nodes) - 1
#         res = ListNode()
#         tail = res
#         while l < r:
#             tail.next = nodes[l]
#             tail.next.next = nodes[r]
#             tail = tail.next.next
#             l += 1
#             r -= 1
#         if l == r:
#             tail.next = nodes[l]
#             tail.next.next = None
#         else:
#             tail.next = None
#         return res.next if res.next else None

        curr = head
        # middle = self.findMiddle(head)
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reversed_head = self.reverseLL(slow)
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
            
        reversed_head = prev
        curr = head
        
        while reversed_head:
            head_next, rev_head_next = curr.next, reversed_head.next
            curr.next = reversed_head
            reversed_head.next = head_next
            reversed_head = rev_head_next
            curr = head_next
        # important! Used to clear any cycle we may have caused with even inputs
        # where the reversed_head's next is assigned to itself with curr.next
        if curr is not None:
            curr.next = None    

#     def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         slow, fast = head, head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow
    
#     def reverseLL(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None
#         while head:
#             next_node = head.next
#             head.next = prev
#             prev = head
#             head = next_node
#         return prev
    
    
            
            
            
            
            
            
            
        
            
        
        