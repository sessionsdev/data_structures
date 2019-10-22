import unittest

from data_structures.queue import Queue

class TestQueue(unittest.TestCase):

    def test_dequeue(self):
        
        # Arrange
        my_queue = Queue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)

        # Act
        dequeue1 = my_queue.dequeue()
        dequeue2 = my_queue.dequeue()


        # Assert
        self.assertEqual(1, dequeue1, "The value is not correct")
        self.assertEqual(2, dequeue2, "The value is not correct")


    def test_enqueue_len(self):

        #Arrange
        my_queue = Queue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)

        #Act
        length = my_queue.__len__()

        #Assert
        self.assertEqual(3, length, "len did not return correct length")