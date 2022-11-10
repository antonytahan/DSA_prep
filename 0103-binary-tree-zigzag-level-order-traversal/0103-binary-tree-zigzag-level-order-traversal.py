# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return root
        q = deque([root])
        res = []
        left_to_right = True
        while q:
            # need a deque here instead of q to append left sometimes
            level_q = deque()
            for i in range(len(q)):
                node = q.popleft()
                # append normally if left_to_right
                if left_to_right:
                    level_q.append(node.val)
                # otherwise we are appending to the left
                else:
                    level_q.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_q)
            # flip parity after each level
            left_to_right = not left_to_right
        return res
                
        