# https://leetcode.com/problems/merge-two-sorted-lists/

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


def merge_ll(list1, list2):
    head = None
    ans = None
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val <= list2.val:
        ans = ListNode(list1.val)
        list1 = list1.next
    else:
        ans = ListNode(list2.val)
        list2 = list2.next

    head = ans
    while list1 and list2:
        if list1.val <= list2.val or list2 == None:
            ans.next = ListNode(list1.val)
            ans = ans.next
            list1 = list1.next
        else:
            ans.next = ListNode(list2.val)
            ans = ans.next
            list2 = list2.next
    if list1:
        ans.next = list1
    elif list2:
        ans.next = list2

    return head


# linkedList = ListNode(1, ListNode(2, ListNode(4)))
# linkedList2 = ListNode(1, ListNode(3, ListNode(4)))
# linkedList_sort = ListNode(1, ListNode(
#     1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
# ans = merge_ll(linkedList, linkedList2)
# print(ans)
# print(linkedList_sort)
