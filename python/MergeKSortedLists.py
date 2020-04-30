from typing import List
# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists is None or len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        dp = [head for head in lists if head is not None and head.val is not None]
        if len(dp) == 0:
            return None
        result = None
        listCount = len(lists)
        head = None
        exitFlag = False
        while not exitFlag:
            minVal = min([node.val for node in dp if node is not None])
            for index, node in enumerate(dp):
                if node and node.val == minVal:
                    dp[index] = node.next
                    break
            if result is None:
                result = ListNode(minVal)
                head = result 
            else:
                head.next = ListNode(minVal)
                head = head.next
            exitFlag = all(node == None for node in dp)
        return result


# ll = ListNode(1)
# ll.next = ListNode(4)
# ll.next.next = ListNode(5)
# input = [ll]
# ll = ListNode(1)
# ll.next = ListNode(3)
# ll.next.next = ListNode(4)
# input.append(ll)
# ll = ListNode(2)
# ll.next = ListNode(6)
# input.append(ll)
# print(Solution().mergeKLists(input))

input = [ListNode(None), ListNode(None)]
print(Solution().mergeKLists(input))