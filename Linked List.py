class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        newNode = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode
    
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        print("Nodes : "+str(total))
    
    def display(self):
        cur = self.head
        ele = []
        while cur.next != None:
            cur = cur.next
            ele.append(cur.data)
        print(ele)

    def get(self, index):
        i=0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if i==index: 
                return cur.data
            i += 1            
        return None

    def delete(self, index):
        i=0
        cur = self.head
        while cur.next != None:
            prev = cur
            cur = cur.next
            if i == index:
                prev.next = cur.next
                return
            i += 1

#Driver 
myList = linkedList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)

myList.length()
myList.display()