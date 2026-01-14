import random

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LL():
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

    def search(self,data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def delete(self,data):
        if not self.head:                               #If the linked list is empty
            return
        if self.head.data == data:                      #If we want to delete the head
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def insert(self,data):
        new_node = Node(data)
        if not self.head:                                            #If Linked list is empty
            self.head = new_node
            return
        
        if self.head.data > data:                                   #If the value is less than the head
            self.head = new_node
            return
        
        current = self.head                                          #Search where to insert, sligthly slicky way
        while current.next and current.next.data < data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

        '''
        while current.next:                                         #Search where to insert, large way
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        current.next = new_node                                     #If we want to insert it to the end
        '''

    def print(self):
        output = []
        current = self.head
        while current:
            output.append(str(current.data))
            current = current.next
        print("->".join(output))

ll = LL()
elements = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(elements)
for e in elements:
    ll.insert(e)
    ll.print()

ll.print()
ll.print()