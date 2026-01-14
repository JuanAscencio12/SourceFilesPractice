'''
A popular inteview question is to find and return the middle node of a linked list
while only traversinfg it once.
So, you're not allowed to traverse it, count the nodes, and then tracerse it again halfway - you get one shot

To find the middle of a linked list, you use a "look ahead" method using two pointers: a fast pointer and a slow pointer.

The first ponter (the "slow pointer") iterates through the list normally. The second pointer iterates two steps 
for every one step the first pointer does. When the second pointer reaches the end of the list,
you simpley return whatever node the slow pointer is currently at.
'''

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
            
    def print(self):
        output = []
        current = self.head
        while current:
            output.append(str(current.data))
            current = current.next
        print("->".join(output))

    def lookAhead(self):
        fast_pointer = self.head
        slow_pointer = self.head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        print(slow_pointer.data)

ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.lookAhead()
ll.print()