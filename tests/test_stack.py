import unittest

from data_structures.stack import Stack


class TestStack(unittest.TestCase):

    def test_push_pop(self):
        
        # Arrange
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        
        # Act
        pop1 = my_stack.pop()
        pop2 = my_stack.pop()
        
        # Assert
        self.assertEqual(2, pop1, "first pop did not have the expected value")
        self.assertEqual(1, pop2, "second pop did not have the expected value")

    def test_push_peek(self):

        #Arrange
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)

        #Act
        peek = my_stack.peek()

        #Assert
        self.assertEqual(2, peek, "peek did not return expected value")


    def test_push_len(self):

        #Arrange
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)

        #Act
        length = my_stack.__len__()

        #Assert
        self.assertEqual(3, length, "len did not return correct length")
    


        