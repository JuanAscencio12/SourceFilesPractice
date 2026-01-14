import random
import sys

#Increasing recursion limit:
#   Not a robust solution
#   stacks take time and memoty to creat
#   much faster to use an iterative solution
#sys.setrecursionlimit(2000)


# With Linked List is better to use iterative solutions
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def search(self,data):
        if self.data == data:
            return True
        if self.next:
            return self.next.search(data)

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:     
            self.head = new_node
            return
        current = self.head     
        while current.next:            
            current = current.next
        current.next = new_node 

    #def searchR(self,data):    # With recursion
    #   return self.head.search(data)

    def search(self,data): # Without recursion
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def print(self):
        output = []
        current = self.head
        while current:
            output.append(str(current.data))
            current = current.next
        print(' -> '.join(output))

def main():
    ll = LinkedList()
    elements = [0,1,2,3,4,5,6,7,8,9]

    random.shuffle(elements)
    for e in elements:
        ll.append(e)
    ll.print()
    print(ll.search(5))
    print(ll.search(10))

if __name__ ==  "__main__":
    main()