import unittest

from data_structures.linked_list import Node, LinkedList


class TestLinkedList(unittest.TestCase):

    def test_insert_front(self):

        #Arrange
        linked_list = LinkedList()

        #Act
        linked_list.insert_front(1)
        linked_list.insert_front(2)

        #Assert
        self.assertEqual(2, linked_list.head.value, "value is not correct")

        

    def test_pop_front(self):

        #Arrange
        linked_list = LinkedList()

        #Act
        linked_list.insert_front(1)
        linked_list.insert_front(2)
        linked_list.pop_front()

        #Assert
        self.assertEqual(1, linked_list.head.value, "value is not correct")

    
    def test_length(self):

        #Arrange
        linked_list = LinkedList()

        #Act
        linked_list.insert_front(1)
        linked_list.insert_front(2)
        linked_list.insert_front(3)
        linked_list.insert_front(5)
        length = linked_list.__len__()

        #Assert
        self.assertEqual(4, length, "value is not correct")


    def test_pop_key(self):

        #Arrange
        linked_list = LinkedList()
        linked_list.insert_front(1)
        linked_list.insert_front(2)
        linked_list.insert_front(3)
        linked_list.insert_front(5)

        #Act
        linked_list.pop_key(2)

        #Assert
        self.assertEqual(3, linked_list.head.next.value, "pop_key did not delect correct node")


    def test_reverse(self):

        #Arrange
        linked_list = LinkedList()
        linked_list.insert_front(1)
        linked_list.insert_front(2)
        linked_list.insert_front(3)
        linked_list.insert_front(4)

        #Act
        linked_list.reverse()

        #Assert
        self.assertEqual(1, linked_list.head.value, "List did not reverse properly")
        self.assertEqual(2, linked_list.head.next.value, "List did not reverse properly")