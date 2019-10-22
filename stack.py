class Stack:

    def __init__(self):
        self._data = list()

    # O(1)
    def push(self, item):
        self._data.append(item)

    # O(n)
    def pop(self):
        item = self._data[len(self._data)-1]
        del self._data[len(self._data)-1]
        return item

    # O(n)    
    def peek(self):
        item = self._data[len(self._data)-1]
        return item

    # O(n)    
    def __len__(self):
        """
        Returns the length of the list
        """
        count = 0
        for _ in self._data:
            count += 1
        return count