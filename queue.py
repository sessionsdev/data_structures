class Queue:
    
    def __init__(self):
        self._data = list()

    # O(1)
    def enqueue(self, item):
        """
        Add item to the queue.
        """
        self._data.append(item)

    # O(1)        
    def dequeue(self):
        """
        Remove item from the queue.
        """
        item = self._data[0]
        del self._data[0]
        return item
    
    # O(n)
    def __len__(self):
        """
        Returns the length of the queue
        """
        count = 0
        for _ in self._data:
            count += 1
        return count