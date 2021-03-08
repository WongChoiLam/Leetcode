# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pre = ListNode(x-1, head)
        lo, hi = pre, head
        while hi != None:
            if hi.val < x:
                lo = lo.next
                hi = hi.next
                continue
            l, n = hi, hi.next
            while n!= None and n.val >= x:
                l = l.next
                n = n.next
            if n == None: break
            lo.next = n
            l.next = n.next
            n.next = hi
            lo, hi = n, hi
        return pre.next