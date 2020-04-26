# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preOrder(root, arr):

    if root is None:
        return
    arr.append(str(root.val))
    if root.left is not None:
        arr.append('(')
        preOrder(root.left, arr)
        arr.append(')')
    if root.right is not None:
        if root.left is None:
            arr.append('()')
        arr.append('(')
        preOrder(root.right, arr)
        arr.append(')')

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        arr = []
        preOrder(t, arr)
        return ''.join(arr)

root = TreeNode(1)
root.right = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
print(Solution().tree2str(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
print(Solution().tree2str(root))

print(print(Solution().tree2str(TreeNode())))