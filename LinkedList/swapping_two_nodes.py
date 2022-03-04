# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head, k: int):
        tmp1 =  head
        tmp2 =  head
        arr = []
        count = 0
        while tmp1:
            arr.append(tmp1.val)
            tmp1 = tmp1.next
            count += 1
        self.swap(k-1 , count - k,arr)

        for i in range(count):
            tmp2.val =  arr[i]
            tmp2 = tmp2.next
        return head
            


    def swap(self,swap1,swap2,arr):
        arr[swap1],arr[swap2] = arr[swap2],arr[swap1]
