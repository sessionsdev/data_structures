import unittest

from data_structures.binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):

    def test_find(self):

        # Arrange
        tree = BinaryTree()


        for i in range(10):
            tree.insert(i)

        # Act

        # Assert

        for i in range(10):
            self.assertEqual(i, tree.get(i))