# https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next
        while index > 0 and curr:
            curr = curr.next
            index -= 1

        if curr and curr != self.right and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, prev, next = ListNode(val), self.left, self.left.next
        node.prev, node.next = prev, next
        next.prev = node
        prev.next = node

    def addAtTail(self, val: int) -> None:
        node, prev, next = ListNode(val), self.right.prev, self.right
        node.prev, node.next = prev, next
        next.prev = node
        prev.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while index > 0 and curr:
            curr = curr.next
            index -= 1

        if index == 0 and curr:
            node, prev = ListNode(val), curr.prev
            node.next, node.prev = curr, prev
            curr.prev = node
            prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while index > 0 and curr:
            curr = curr.next
            index -= 1

        if index == 0 and curr and curr != self.right:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

    def returnArray(self) -> list:
        ans = []
        curr = self.left.next
        while curr.next:
            ans.append(curr.val)
            curr = curr.next
        return ans


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)
# print(obj.get(1))
# print(obj.returnArray())
# obj.deleteAtIndex(1)
# print(obj.returnArray())
