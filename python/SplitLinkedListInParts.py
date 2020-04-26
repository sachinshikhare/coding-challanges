# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if root == None or k <= 0:
            return None
        if k <= 1:
            return [root]

        length = 0
        temp = root
        while temp is not None:
            length += 1
            temp = temp.next

        partitionLength = length // k
        remainder = length % k

        result = [None] * k
        prev = None
        head = root
        for i in range(k):
            result[i] = head
            for j in range(partitionLength + (1 if i <= (remainder - 1) else 0)):
                prev = head
                head = head.next
            if prev is not None:
                prev.next = None
        return result


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
print(Solution().splitListToParts(root, 5))
