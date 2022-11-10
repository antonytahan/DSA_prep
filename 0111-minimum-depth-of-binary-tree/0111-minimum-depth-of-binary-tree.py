# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        min_depth = 0
        while q:
            min_depth += 1
            for i in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return min_depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        