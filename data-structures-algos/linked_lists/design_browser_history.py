class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.current
        self.current.next = node
        self.current = node

    def back(self, steps: int) -> str:
        curr = self.current
        while steps > 0 and curr.prev:
            curr = curr.prev
            steps -= 1
        self.current = curr
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.current
        while steps > 0 and curr.next:
            curr = curr.next
            steps -= 1
        self.current = curr
        return curr.val

    def printHist(self):
        ans = []
        temp = self.current
        while temp:
            ans.insert(0, temp.val)
            temp = temp.prev
        temp = self.current.next
        while temp:
            ans.append(temp.val)
            temp = temp.next
        return ans


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory('leetcode.com')
# obj.visit('google.com')
# obj.visit('facebook.com')
# obj.visit('youtube.com')
# print(obj.printHist())
# print(obj.back(1))
# print(obj.back(1))
# print(obj.forward(1))
# obj.visit('linkedin.com')
# print(obj.printHist())
# print(obj.forward(2))
# print(obj.back(2))
# print(obj.back(7))
# print(obj.printHist())
