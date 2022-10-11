# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False
        
        xinfo = []
        yinfo = []
        parent = None
        level = 0
        
        self.dfs(x, y, root, None, 0, xinfo, yinfo)
        
        return xinfo[0][0] == yinfo[0][0] and xinfo[0][1] != yinfo[0][1]
        
    def dfs(self, x, y, root, parent, level, xinfo, yinfo):
        if root is None:
            return None
        
        if root.val == x:
            xinfo.append((level, parent))
        if root.val == y:
            yinfo.append((level, parent))
            
        self.dfs(x, y, root.left, root, level+1, xinfo, yinfo)
        self.dfs(x, y, root.right, root, level+1, xinfo, yinfo)
        