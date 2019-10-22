class Node:


    def __init__ (self, value = None, next_node = None, prev_node = None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList:


    def __init__(self):
        self.first_node = None
        

    # O(1)    
    def insert_front(self, value):

        """Function to insert new Node to from of doubly linked list
        
        Arguments:
            value {[Any]} -- Stored value of memory node
        """

        new_node = Node(value = value, next_node=self.first_node)
        if self.first_node:
            self.first_node.prev_node = new_node
        self.first_node = new_node

    # O(n)    
    def insert_back(self, value):
        if not self.first_node:
            self.first_node = Node(value=value)
            return
        current = self.first_node
        while current.next_node:
            current = current.next_node
        current.next_node = Node(value=value, prev_node=current)

    # O(1)    
    def pop_front(self):
        if self.first_node == None:
            return
        if self.first_node.next_node == None:
            self.first_node = None
            return
        self.first_node = self.first_node.next_node
        self.first_node.prev_node = None
    
    # O(n)
    def pop_back(self):
        if self.first_node == None:
            return
        if self.first_node.next_node == None:
            self.first_node = None
            return
        current = self.first_node
        while current.next_node is not None:
            current = current.next_node
        current.prev_node.next_node = None

    # O(n)
    def __repr__(self):
        nodes = []
        current = self.first_node
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return "[" + ",".join(nodes) + "]"
