#Breadth first search
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

#Method1
def getValuesByLevel(root):
    output = []
    queue = [[root,0]]
    i=0
    while i < len(queue):
        poppedNode = queue[i][0]
        level = queue[i][1]
        i += 1
        if poppedNode is None:
            continue
        else:
            if len(output) <= level:
                output.append([])
            output[level].append(poppedNode.val)
            queue.append([poppedNode.left, level+1])
            queue.append([poppedNode.right, level+1])
    return output

#Driver code

root = Node(5)
root.left = Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(7)
ans = getValuesByLevel(root)
print(ans)