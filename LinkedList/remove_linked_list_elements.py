# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
            else:
                prev = nxt
            curr = nxt
        return dummy.next