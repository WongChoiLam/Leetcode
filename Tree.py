class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def listToTree(lst):
    if len(lst) == 0: return None
    index = 1
    root = TreeNode(lst[0])
    level_node = [root]
    
    while index < len(lst):
        level_index = 0
        prev = level_node
        level_node = []
        while index < len(lst) and level_index < len(prev):
            if(lst[index] != None):
                leftNode = TreeNode(lst[index])
                prev[level_index].left = leftNode
                level_node.append(leftNode)
            index += 1
            if(index < len(lst)):
                if(lst[index] != None):
                    rightNode = TreeNode(lst[index])
                    prev[level_index].right= rightNode
                    level_node.append(rightNode)
                index += 1
            level_index += 1
    return root

def treeToList(root : TreeNode):
    if root == None: return []
    ans = [root.val]
    level = [root]
    while len(level) > 0:
        prev = level
        level = []
        for node in prev:
            if(node.left != None):
                ans.append(node.left.val)
                level.append(node.left)
            else:
                ans.append(None)
            if(node.right!= None):
                ans.append(node.right.val)
                level.append(node.right)
            else:
                ans.append(None)
    return ans