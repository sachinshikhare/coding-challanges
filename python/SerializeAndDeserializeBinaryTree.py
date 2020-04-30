import math

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class Codec:


    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        result = []
        self.bfs(root, result)
        return result

    def getHeight(self, root):
        if root is None:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def bfs(self, root, result):
        height = self.getHeight(root)
        for level in range(height + 1):
            self.traverseGivenLevel(root, level, result)



    def insertLevelOrder(self, data, root, index, length):
        if index < length:
            if data[index] is None:
                return None
            root = TreeNode(data[index])
            root.left = self.insertLevelOrder(data, root.left, index * 2 + 1, length)
            root.right = self.insertLevelOrder(data, root.right, index * 2 + 2, length)
        return root


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.insertLevelOrder(data, None, 0, len(data))

    def traverseGivenLevel(self, root, level, result):
        if root is None:
            result.append(None)
            return
        if level == 1:
            result.append(root.val)
            return
        if level > 1:
            self.traverseGivenLevel(root.left, level - 1, result)
            self.traverseGivenLevel(root.right, level - 1, result)


# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
codec = Codec()
codec.deserialize(codec.serialize(root))


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(3)
root.right.left.right = TreeNode(1)
print(codec.serialize(root))
codec.deserialize(codec.serialize(root))

