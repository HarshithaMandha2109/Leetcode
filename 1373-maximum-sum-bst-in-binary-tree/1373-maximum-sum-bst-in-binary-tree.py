# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode | None) -> int:
        #self.total=0
        self.ans=0
        def dfs(node):
            if node is None:
                return (float("inf"),float("-inf"),0)
            left_min,left_max,left_sum=dfs(node.left)
            right_min,right_max,right_sum=dfs(node.right)
            if left_max<node.val<right_min:
                total=left_sum+right_sum+node.val
                self.ans=max(self.ans,total)
                return (min(left_min,node.val),max(right_max,node.val),total)
            return (float("-inf"),float("inf"),0)
        dfs(root)
        return self.ans
        