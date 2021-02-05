class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listToLinkedList(lst):
    if len(lst) == 0 : return None
    head = ListNode(lst[0])
    tail = head
    for val in lst[1:]:
        tail.next = ListNode(val)
        tail = tail.next
    return head