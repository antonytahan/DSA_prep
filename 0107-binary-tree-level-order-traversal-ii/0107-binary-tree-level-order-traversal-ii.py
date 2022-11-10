# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        # initialize deque with root
        q = deque([root])
        res = []
        while q:
            # create a level list to append all nodes in the same level to
            level = []
            # pop all original members of q and append to level
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                # add new nodes to queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # append level list to result
            res.append(level)
        return res[::-1]
