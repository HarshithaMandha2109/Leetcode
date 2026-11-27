# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        def check(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val!=right.val:
                return False
            return check(left.left,right.right) and check(right.left,left.right)
        return check(root.left,root.right)
        













        return check(root.left,root.right)
        def check(left,right):
            if not left and not right:
                return False
            if left.value!=right.value:
                return False
            return check(left.left,left.right)and check(right.left,right.right)
        