
class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def createTree(self, nodes: list(int)):
        treenode = Node()

        for element in nodes:
            if element < treenode.val:
                temp = Node(element,None, None)
                treenode.left = temp
            elif element > treenode.val:
                temp = Node(element, None, None)
                treenode.right = temp

        return treenode

if __name__ == '__main__':
    S = Tree()
    print(S.createTree([]))