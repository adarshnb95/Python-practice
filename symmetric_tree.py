# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # inorder, but reverse
        
        def inorder(root):
            
            elements = []
            if root.left:
                elements = elements + inorder(root.left)
            else:
                elements.append(None)
            
            
            elements.append(root.val)
            
            if root.right:
                elements = elements + inorder(root.right)
            else:
                elements.append(None)
            
            return elements
        
        
        def inorderreverse(root):
            elements = []
            if root.right:
                elements = elements + inorderreverse(root.right)
            else:
                elements.append(None)
            
            elements.append(root.val)
            
            if root.left:
                elements = elements + inorderreverse(root.left)
            else:
                elements.append(None)
                
            return elements
        
        
        leftTree = []
        rightTree = []
        
        # for left tree
        if root.left  and root.right:
            leftTree = inorder(root)
            rightTree = inorderreverse(root)
            
            print(leftTree, rightTree)
            
            if leftTree == rightTree:
                return True
            else:
                return False
        
        return True


if __name__ == "__main__":
    S = Solution()

    print(S.levelOrder([3,9,20,null,null,15,7]))