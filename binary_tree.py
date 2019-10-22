class BinaryTree:

    def __init__(self):
        self.head = None


    def insert(self, data):
        current = self.head
        previous = None
        if current is None:
            self.head = Node(data=data)
            return
        # if data < current.data and current.l_child is None:
        #     current.l_child = Node(data, current)
        # if data >= current.data and current.r_child is None:
        #     current.r_child = Node(data, current)
        while current:
            if data < current.data:
                previous = current        previous.child = current        previous.child = current
                current = current.l_child
            elif data >= current.data:
                previous = current
                current = current.r_child
        current = Node(data=data)
            





    def get(self, key):
        pass




    def rebalance(self):
        pass

class Node:

    def __init__(self, data, l_child=None, r_child=None ):
        self.data = data
        self.l_child = l_child
        self.r_child = r_child


tree = BinaryTree()

tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(5)

print(tree.head.data)
# print(tree.head.l_child.parent.data)
# print(tree.head.l_child.data)
print(tree.head.r_child)