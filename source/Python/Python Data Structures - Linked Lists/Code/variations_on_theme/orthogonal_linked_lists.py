class ONode:
    def __init__(self, data, row, col):
        self.data = data
        self.row = row
        self.col = col
        self.down = None
        self.right = None

class OLL:
    def __init__(self, rows, cols):
        self.row_head = [ONode(None, i, -1) for i in range(0,rows)]
        self.col_head = [ONode(None, -1, i) for i in range(0,cols)]

    def insert(self, new_node):
        current = self.row_head[new_node.row]
        while current.right  and current.right.col < new_node.col:
            current = current.right
        new_node.right = current.right
        current.right = new_node

        current = self.col_head[new_node.col]
        while current.down  and current.down.row < new_node.row:
            current = current.down
        new_node.down = current.down
        current.down = new_node

    def print(self):
        for row in self.row_head:
            output = ['0'] * len(self.col_head)
            current = row
            while current.right:
                current = current.right
                output[current.col] = str(current.data)
            
            print(' '.join(output))


oll = OLL(4,5)
oll.insert(ONode(3,0,0))
oll.insert(ONode(4,0,4))
oll.insert(ONode(2,1,2))
oll.insert(ONode(1,2,1))

oll.print()