#Reverse binary tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

#Method 1
def reverseTree(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    reverseTree(root.left)
    reverseTree(root.right)

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

#Driver code

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Before reverse")
inOrder(root)

print("After reverse")
inOrder(root)