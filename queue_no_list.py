from data_structures.stack import Stack

class Queue:

    def __init__(self):
        self._stack_1 = Stack()
        self._stack_2 = Stack()


    def enqueue(self, data):
        stack_1 = self._stack_1
        stack_2 = self._stack_2
        if len(stack_1) == 0:
            move(stack_1, stack_2)
        stack_1.push(data)


    def dequeue(self):
        stack_1 = self._stack_1
        stack_2 = self._stack_2
        if len(stack_2) == 0:
            move(stack_1, stack_2)
        return stack_2.pop() 



def move(s1, s2):
    while len(s1):
        item = s1.pop()
        s2.push(item)
        return
    while len(s2):
        item = s2.pop()
        s1.push(item)
        return




