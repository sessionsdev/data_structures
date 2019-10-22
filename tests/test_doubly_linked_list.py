import unittest

from data_structures.doubly_linked_list import Node, DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def test_insert_front(self):
        
        #Arrange
        double_linked = DoublyLinkedList()

        #Act
        double_linked.insert_front(1)
        double_linked.insert_front(2)
        double_linked.insert_front(3)

        #Assert
        self.assertEqual(3, double_linked.first_node.value, "The value returned is not correct")
        self.assertEqual(None, double_linked.first_node.prev_node, "The value returned is not correct")

    def test_insert_back(self):
        
        #Arrange
        double_linked = DoublyLinkedList()

        #Act
        double_linked.insert_back(3)
        double_linked.insert_back(2)
        double_linked.insert_back(1)

        #Assert
        self.assertEqual(3, double_linked.first_node.value, "The value returned is not correct")


    def test_pop_front(self):
        
        #Arrange
        double_linked = DoublyLinkedList()
        double_linked.insert_front(1)
        double_linked.insert_front(2)
        double_linked.insert_front(3)

        #Act
        double_linked.pop_front()


        #Assert
        self.assertEqual(2, double_linked.first_node.value, "pop_front did not return the correct node value")
        self.assertEqual(None, double_linked.first_node.prev_node, "pop_front did not return the correct node value")


    def test_pop_back(self):
        
        #Arrange
        double_linked = DoublyLinkedList()
        double_linked.insert_front(1)
        double_linked.insert_front(2)

        #Act
        double_linked.pop_back()


        #Assert
        self.assertEqual(None, double_linked.first_node.next_node, "pop_back did not return correct node value")