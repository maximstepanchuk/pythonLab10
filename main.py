class newNode:
    def __init__(self, x, y):
        self.keyX = x
        self.keyY = y
        self.left = None
        self.right = None

def deleteNegativeNodes(root):

    if root == None:
        return None

    root.left = deleteNegativeNodes(root.left)
    root.right = deleteNegativeNodes(root.right)
    if (root.keyX < 0) & (root.keyY < 0):
        rChild = root.right
        return rChild

    if (root.keyX < 0) & (root.keyY < 0):
        lChild = root.left
        return lChild

    return root

def showPositivesY(root):
    if root.keyY > 0:
        inorderTraversal(root.left)
        print(root.keyX, root.keyY, end=" ")
        print()
        inorderTraversal(root.right)
    else:
        print("----")

def insert(root, keyX, keyY):
    if root == None:
        return newNode(keyX, keyY)
    if root.keyY > keyY:
        root.left = insert(root.left, keyX, keyY)
    else:
        root.right = insert(root.right, keyX, keyY)
    return root

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.keyX, root.keyY, end=" ")
        print()
        inorderTraversal(root.right)

if __name__ == '__main__':
    root = None
    root = insert(root, -665546, -5454618)
    root = insert(root, -16433, 10)
    root = insert(root, 14, 15)
    root = insert(root, -8, -7)
    root = insert(root, -15, -12364)
    root = insert(root, 13, 45 )
    root = insert(root, 7, 486)

    print()
    print("Inorder traversal of the modified tree is:",
          end=" ")
    inorderTraversal(root)

    print("------------------------------------")
    showPositivesY(root)
    print("------------------------------------")
    root = deleteNegativeNodes(root)
    print()

    print("Inorder traversal of the modified tree is:",
          end=" ")
    inorderTraversal(root)

