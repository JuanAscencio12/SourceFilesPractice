class Node:
    def __init__(self, data, name):
        self.data = data
        self.name = name
        self.next = None

#To have a collection of nodes
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data, name):
        new_node = Node(data, name)
        if not self.head:               #In case our head is None
            self.head = new_node
            return
        current = self.head             #To keep track of where is the last element
        while current.next:             #Check if in fact we are in the last element
            current = current.next
        current.next = new_node         #If it is, we append a new node with data

    def print(self):
        output = []
        current = self.head
        while current:
            output.append(str(current.data))
            output.append(str(current.name))
            current = current.next
        print(' -> '.join(output))

# Simple linked list
n = Node(1,'A')
n.next = Node(2,'B')
n.next.next = Node(3,'C')

print(n.data, n.name)
print(n.next.data, n.next.name)
print(n.next.next.data, n.next.next.name)

# Linked list
ll = LinkedList()

ll.append(1,'D')
ll.append(2,'E')
ll.append(3,'F')
ll.append(4,'G')
ll.append(5,'H')
ll.append(6,'I')
ll.print()