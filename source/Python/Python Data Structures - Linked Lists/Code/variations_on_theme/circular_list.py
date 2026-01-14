class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = self.head
            self.head.next = self.head
            return

        self.tail.next = newNode
        newNode.next = self.head
        self.tail = newNode

    def print(self):
        if not self.head:
            return
        output = []
        current = self.head
        while current.next != self.head:
            output.append(str(current.data))
            current = current.next
        output.append(str(self.tail.data))            
        print(" -> ".join(output) + '-> ...')

cll = CLL()
elements = [0,1,2,3,3,3,4,4,5,6,7,8,9,9,9]
for e in elements:
    cll.append(e)

cll.print()