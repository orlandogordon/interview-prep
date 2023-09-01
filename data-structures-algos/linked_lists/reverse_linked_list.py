# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, value=0, next=None) -> None:
        self.val = value
        self.next = next

    def create_arr(self):
        output = []
        head = self
        while head:
            output.append(head.val)
            head = head.next
        return output


def reverse_ll(head):
    if head:
        rev = ListNode(head.val)
        while head.next:
            head = head.next
            rev = ListNode(head.val, rev)
        return rev
    else:
        return head


linkedList2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
linkedList1_rev = ListNode(5, ListNode(
    4, ListNode(3, ListNode(2, ListNode(1)))))
ans = reverse_ll(linkedList)
print(linkedList1_rev)
print(reverse_ll(linkedList) == linkedList1_rev)
print(ans.create_arr())
