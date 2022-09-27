import numbers


class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def addChild(self, child):
        if self.val == child:
            return
        
        if child < self.val:
            if self.left:
                self.left.addChild(child)
            else:
                self.left = TreeNode(child)
        
        elif child > self.val:
            if self.right:
                self.right.addChild(child)
            else:
                self.right = TreeNode(child)
    
    def inOrderTraversal(self):
        elements = []
        # traverse left
        if self.left:
            elements = elements + self.left.inOrderTraversal()
        
        #get mid
        elements.append(self.val)

        # traverse right
        if self.right:
            elements = elements + self.right.inOrderTraversal()

        return elements

def buildTree(elements):
    root = TreeNode(elements[0])
    for i in range(1, len(elements)):
        root.addChild(elements[i])
    return root

if __name__ == '__main__':
    nums = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = buildTree(nums)
    print(numbers_tree.inOrderTraversal())    