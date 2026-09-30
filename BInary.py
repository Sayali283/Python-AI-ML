#program to create binary tree
#node class
class node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
#create binary tree
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
#Inorder Traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
print("\nInorder Traversal:")
inorder(root)
#preorder Traversal
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
print("\nPreorder Traversal:")
inorder(root)
#Postorder Traversal
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
print("\nPostorder Traversal:")
postorder(root)
