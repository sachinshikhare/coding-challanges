# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k == 0:
            return head

        length = self.getLength(head)
        if k >= length:
            k %= length

        newHeadIndex = length - k
        if newHeadIndex == length:
            return head
        i = 0
        tempHead = head
        while i < newHeadIndex:
            prev = head
            head = head.next
            i += 1
        newHead = head
        prev.next = None
        temp = newHead
        while temp.next is not None:
            temp = temp.next

        temp.next = tempHead
        return newHead


    def getLength(self, head):
        length = 0
        while head is not None:
            head = head.next
            length += 1
        return length


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
Solution().rotateRight(head, 10)