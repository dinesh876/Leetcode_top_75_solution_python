# Node definition
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

# Creating linked List    
a  = Node(1)
b  = Node(2)
c  = Node(3)
d =  Node(4)

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d


# Logic to reverse a List
class Solution:
    def reverseList(self,head):
        prev  = None
        current = head
        while current:
            next = current.next
            current.next  = prev
            prev = current
            current = next
        return prev

reverse = Solution().reverseList(a)

# Print Reverse List
while reverse:
    print(reverse.val)
    reverse = reverse.next