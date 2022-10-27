class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = []
            
        if not root.left and not root.right and k == 1:
            return root.val
        
        def dfs(root, elements):
            if not root.left and not root.right:
                elements.append(root.val)
                return
            if root.left:
                dfs(root.left, elements)
            if root.right:
                dfs(root.right, elements)
        
        
        
        dfs(root, elements)
        elements.sort()
        
        
        return elements[k-1]
        