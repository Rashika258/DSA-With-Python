# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def DFS(node):
            if node == None:
                return None
            self.result = self.result + 1

            DFS(node.left)
            DFS(node.right)

        DFS(root)
        return self.result
        # if root is None:
        #     return 0
        # return 1+ self.countNodes(root.left)+ self.countNodes(root.right)
        