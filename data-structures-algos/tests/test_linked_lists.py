import pytest
from linked_lists.reverse_linked_list import reverse_ll
from linked_lists.merge_two_lists import merge_ll
from linked_lists.design_linked_list import MyLinkedList
from linked_lists.design_browser_history import BrowserHistory

# https://realpython.com/pytest-python-testing/#what-makes-pytest-so-useful


class ListNode:
    def __init__(self, value=0, next=None) -> None:
        self.val = value
        self.next = next


class TestLinkedLists:
    linkedList1 = ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5)))))
    linkedList2 = ListNode(1, ListNode(2, ListNode(4)))
    linkedList3 = ListNode(1, ListNode(3, ListNode(4)))

    def test_reverse_ll(self):
        assert reverse_ll(self.linkedList1).create_arr() == [5, 4, 3, 2, 1]

    def test_merge_ll(self):
        assert merge_ll(self.linkedList2, self.linkedList3).create_arr() == [
            1, 1, 2, 3, 4, 4]

    def test_design_ll(self):
        obj = MyLinkedList()
        obj.addAtHead(1)
        obj.addAtTail(3)
        obj.addAtIndex(1, 2)
        assert obj.get(1) == 2
        obj.deleteAtIndex(1)
        assert obj.returnArray() == [1, 3]

    def test_design_browser_history(self):
        obj = BrowserHistory('leetcode.com')
        obj.visit('google.com')
        obj.visit('facebook.com')
        obj.visit('youtube.com')
        assert obj.printHist() == ['leetcode.com',
                                   'google.com', 'facebook.com', 'youtube.com']

        ans = []
        ans.append(obj.back(1))
        ans.append(obj.back(1))
        ans.append(obj.forward(1))
        assert ans == ["facebook.com", "google.com", "facebook.com"]

        obj.visit('linkedin.com')
        assert obj.printHist() == ['leetcode.com',
                                   'google.com', 'facebook.com', 'linkedin.com']

        assert obj.back(7) == 'leetcode.com'
        assert obj.printHist() == ['leetcode.com',
                                   'google.com', 'facebook.com', 'linkedin.com']
