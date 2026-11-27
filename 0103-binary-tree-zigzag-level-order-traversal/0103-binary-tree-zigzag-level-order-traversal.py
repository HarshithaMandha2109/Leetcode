# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        q=deque([root])
        traversal=[]
        zig=False
        while q:
            level=len(q)
            temp=[]
            for _ in range(level):
                node=q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if zig:
                temp.reverse()
            traversal.append(temp)
            zig=not zig
        return traversal

        