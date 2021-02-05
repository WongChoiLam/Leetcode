from typing import List
from Tree import *
from LinkedList import *
class Solution:
    def subPath(self, tree: TreeNode, expected: List[ListNode], head: ListNode) -> bool:
        if None in expected: return True
        if tree==None: return False
        i = 0
        print(tree.val, [n.val for n in expected])
        while i < len(expected):
            if(expected[i].val == tree.val):
                # print("\t",expected[i].val)
                expected[i] = expected[i].next
                i += 1
            else:
                del expected[i]
        expected.append(head)
        return self.subPath(tree.left, expected.copy(), head) or self.subPath(tree.right, expected.copy(), head)
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        return self.subPath(root, [head], head)

null = None

s = Solution()
root = listToTree([1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3])
linkedList = listToLinkedList([1,4,2,6])
print(s.isSubPath(linkedList, root))

root = listToTree([1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3])
linkedList = listToLinkedList([4,2,8])
print(s.isSubPath(linkedList, root))

