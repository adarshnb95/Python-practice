# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        result = []
        sumofpath = 0
        path = []
        self.dfs(root, sumofpath, targetSum, path, result)
        return result
        
    def dfs(self, root, sumofpath, targetSum, path, result):
        if root is None:
            return None
        sumofpath += root.val
        
        if root.left is None and root.right is None and sumofpath == targetSum:
            result.append([*path, root.val])
            return None
        
        path.append(root.val)
        self.dfs(root.left, sumofpath, targetSum, path, result)
        self.dfs(root.right, sumofpath, targetSum, path, result)
        sumofpath -= root.val
        path.pop()

