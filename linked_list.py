class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class LinkedList:
    
    def __init__(self):
        self.head = None
        
    
    # O(1)
    def insert_front(self, value):
        """
        Insert an item at the front of the queue
        """
        self.head = Node(value = value, next = self.head)

    # O(1)
    def pop_front(self):
        """
        Remove an item from the front
        """
        if self.head != None:
            value = self.head.value
            self.head = self.head.next
            return value

    # O(n)
    def pop_key(self, key):
        current = self.head
        if current.value == key:
            temp = self.head
            self.head = current.next
            return temp
        while key != current.next.value:
            current = current.next
        if current.next or current.next.next != None:
            return
        else:
            current.next = current.next.next

    def pop_at_index(self, index):
        prev = None
        current = self.head
        counter = 1
        while counter != index:
            prev = current
            current = current.next
            counter += 1
        current.prev = current.next

        
            

    def find_key(self, key):
        pass

    # O(n)    
    def __len__(self):
        """
        Returns the length of the list
        """
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    # O(n)
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    
    # O(n)
    def __repr__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.value))
            current = current.next
        return "[" + ", ".join(nodes) + "]"

