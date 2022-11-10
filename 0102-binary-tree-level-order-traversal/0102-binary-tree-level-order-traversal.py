# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
    ##recursive:
#         if not root:
#             return root
#         res = []
        
#         def dfs(root, level):
#             if len(res) == level:
#                 res.append([])
            
#             res[level].append(root.val)
#             if root.left:
#                 dfs(root.left, level + 1)
#             if root.right:
#                 dfs(root.right, level + 1)
        
#         dfs(root, 0)
#         return res
    
         
        #iterative
#         if not root:
#             return root
#         res = []
#         stack = deque([(0, root)])
#         while stack:
#             level, node = stack.popleft()
#             res.append([node.val])
#             if node.left:
#                 stack.append((level + 1, node.left))
#             if node.right:
#                 stack.append((level + 1,node.right))
#             while stack and stack[0][0] == level:
#                 _, new_node = stack.popleft()
#                 res[level].append(new_node.val)
#                 if new_node.left:
#                     stack.append((level + 1, new_node.left))
#                 if new_node.right:
#                     stack.append((level + 1,new_node.right))
#             level += 1             
#         return res


        # #cleaner iterative:
        # res = []
        # q = deque()
        # q.append(root)
        # while q:
        #     level = []
        #     level_length = len(q)
        #     for i in range(level_length):
        #         node = q.popleft()
        #         if node:
        #             level.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     if level:
        #         res.append(level)
        # return res
        
####-------- revisit---------

        #recursive
#         if not root:
#             return root
#         res = []
#         def dfs(root, level):
#             if len(res) == level:
#                 res.append([])
            
#             res[level].append(root.val)
#             if root.left:
#                 dfs(root.left, level + 1)
#             print(res)
#             if root.right:
#                 dfs(root.right, level + 1)
#         dfs(root, 0)
#         return res

        #iterative:
        # if root is None:
        #     return root
        # q = deque([root])
        # res = []
        # level = 0
        # while q:
        #     res.append([])
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         res[level].append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return res
        
        
        if not root:
            return root
        q = deque([root])
        res = []
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
        
        
                
            
            
            
            
        
   
        
        
        