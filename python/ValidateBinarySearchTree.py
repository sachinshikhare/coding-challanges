# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.prevInorder = None
    def isValidBST(self, root: TreeNode) -> bool:

        if not root:
            return True

        left = self.isValidBST(root.left)

        if not left:
            return False

        if self.prevInorder is not None and self.prevInorder >= root.val:
            return False
        else:
            self.prevInorder = root.val

        right = self.isValidBST(root.right)
        if not right:
            return False

        return  left and right


# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
# print(Solution().isValidBST(root))
#
# root = TreeNode(5)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.right = TreeNode(6)
# root.right.left = TreeNode(3)
# print(Solution().isValidBST(root))
#
# print(Solution().isValidBST(None))
#
# root = TreeNode(1)
# root.left = TreeNode(1)
# print(Solution().isValidBST(root))
#
# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(15)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(20)
# print(Solution().isValidBST(root))

root = TreeNode(0)
root.right = TreeNode(-1)
print(Solution().isValidBST(root))