from LinkedList import *
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre_ans = ListNode(next=head)
        pre = None
        start = head
        index = 1
        while index != m:
            pre = start
            start = start.next
            index += 1
        current_node = start
        next_node = start.next
        while index < n:
            next_next_node = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = next_next_node
            index += 1
        end = current_node
        suffix = next_node
        start.next = suffix
        if pre != None:
            pre.next = end
            return head
        return end
        