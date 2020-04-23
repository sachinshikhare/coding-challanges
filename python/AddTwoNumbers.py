# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = "0"
        result = ListNode(0)
        movingPointer = result
        while l1 is not None and l2 is not None:
            temp = str(l1.val + l2.val + int(carry))
            if len(temp) > 1:
                carry = temp[0]
                sum = temp[1]
            else:
                carry = "0"
                sum = temp[0]
            movingPointer.next = ListNode(int(sum))
            movingPointer = movingPointer.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            temp = str(int(carry) + l1.val)
            if len(temp) > 1:
                carry = temp[0]
                sum = temp[1]
            else:
                carry = "0"
                sum = temp[0]
            movingPointer.next = ListNode(int(sum))
            movingPointer = movingPointer.next
            l1 = l1.next
        while l2 is not None:
            temp = str(int(carry) + l2.val)
            if len(temp) > 1:
                carry = temp[0]
                sum = temp[1]
            else:
                carry = "0"
                sum = temp[0]
            movingPointer.next = ListNode(int(sum))
            movingPointer = movingPointer.next
            l2 = l2.next
        if carry is not "0":
            movingPointer.next = ListNode(int(carry))
        return result.next

# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
#
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
#
# result = Solution().addTwoNumbers(l1, l2)

l1 = ListNode(1)


l2 = ListNode(9)
l2.next = ListNode(9)

result = Solution().addTwoNumbers(l1, l2)
print(result.val, result.next.val, result.next)