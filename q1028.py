# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def split(S: str) -> (str, str):
            index = 0
            word_len = 0
            while S[index] == '-':
                index += 1
            while (index + word_len) < len(S) and S[index + word_len] != '-':
                word_len += 1
            return index + 1, S[index:index + word_len], S[index + word_len:]
        if len(S) == 0:return None
        level = 1
        l, val, S = split(S)
        backtrack = [TreeNode(val)]
        root = backtrack[0]
        while len(S) > 0:
            l, val, S = split(S)
            node = TreeNode(val)
            while l != (level + 1):
                backtrack = backtrack[0:-1]
                level -= 1
            parent = backtrack[-1]
            if parent.left == None: parent.left = node
            else: parent.right = node
            backtrack.append(node)
            level += 1
        return root

Solution().recoverFromPreorder("1-401--349---90--88")