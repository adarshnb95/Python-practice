# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return None
        
        res = [[]]
        level = 0
        self.zigzagtraverse(root, res, level)
        return res
        
    def zigzagtraverse(self, root, res, level):
        if root is None:
            return None
        
        if len(res)< level+1:
            res.append([])
            
        if level%2 == 1:
            res[level].append(root.val)
        else:
            res[level].insert(0, root.val)
        
        self.zigzagtraverse(root.right, res, level+1)
        self.zigzagtraverse(root.left, res, level+1)
        