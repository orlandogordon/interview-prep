import pytest
from linked_lists.reverse_linked_list import reverse_ll

# https://realpython.com/pytest-python-testing/#what-makes-pytest-so-useful


class ListNode:
    def __init__(self, value=0, next=None) -> None:
        self.val = value
        self.next = next


class TestLinkedLists:
    linkedList1 = ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5)))))

    def test_reverse_ll(self):
        assert reverse_ll(self.linkedList1).create_arr() == [5, 4, 3, 2, 1]
