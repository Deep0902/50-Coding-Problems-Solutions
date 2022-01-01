#Depth first tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

def preOrder(root):
    if root is None:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)

#Driver code

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\nInorder\n")
inOrder(root)

print("\nPreorder\n")
preOrder(root)

print("\npostorder\n")
postOrder(root)