# import unittest

# from data_structures.dictionary import Dictionairy

# class TestDictionary(unittest.TestCase):


#     def test_get_index(self):

#         # Arrange
#         d = Dictionairy(100)

#         # Act
#         index1 = d.get_index("One")
#         index2 = d.get_index("hello")
#         index3 = d.get_index(5)
#         test1 = index1 >= 0 and index1 < 100
#         test2 = index2 >= 0 and index2 < 100
#         test3 = index3 >= 0 and index3 < 100

#         # Assert
#         self.assertEqual(index1, d.get_index("One"), "Hash function did not return same value")
#         self.assertEqual(index2, d.get_index("hello"), "Hash function did not return same value")
#         self.assertEqual(index3, d.get_index(5), "Hash function did not return same value")
#         self.assertTrue(test1, "Index 1 is not between 0 and 100")
#         self.assertTrue(test2, "Index 2 is not between 0 and 100")
#         self.assertTrue(test3, "Index 3 is not between 0 and 100")
        

#     def test_set(self):

#         # Arrange
#         d = Dictionairy(100)

#         # Act
#         d.set("one", 1)
#         d.set("Two", 2)
#         d.set("three", "dog")

#         # Assert
#         self.assertEqual(1, d.get("one"), "Dictionary did not get correct value")
#         self.assertEqual(2, d.get("Two"), "Dictionary did not get correct value")
#         self.assertEqual("dog", d.get("three"), "Dictionary did not get correct value")
#         self.assertEqual(d.set("one", "one"), None, "Dictionary allows duplicates")


#     def test_get(self):

#         # Arrange
#         d = Dictionairy(100)
#         d.set("one", 1)
#         d.set("two", 2)
        
        
#         # Act
#         value1 = d.get("one")
#         value2 = d.get("two")

#         # Assert
#         self.assertEqual(1, value1, "get did not retrieve correct value")
#         self.assertEqual(2, value2, "get did not retrieve correct value")



#     def test_contains(self):

#         # Arrange
#         d = Dictionairy(100)
#         d.set("one", 1)
#         d.set("two", 2)

#         # Act
#         result = d.contains("one")
#         result2 = d.contains("two")
#         result3 = d.contains("three")

#         # Assert
#         self.assertEqual(result, True, "contains did not find key")
#         self.assertEqual(result2, True, "contains did not find key")
#         self.assertEqual(result3, False, "contains found key that doesn't exsist")


#     def test_delete(self):

#         # Arrange        
#         d = Dictionairy(100)
#         d.set("one", 1)
#         d.set("two", 2)

#         # Act
#         d.delete("one")
#         d.delete("two")

#         # Assert
#         self.assertEqual(d.get("one"), None, "delete did not remove key")
#         self.assertEqual(d.get("two"), None, "delete did not remove key")




#     def test_expand(self):

#             d = Dictionairy(10000)
#             for i in range(1, 1000000):
#                 d.set(str(i), i)

#             # Act
#             # d.expand()

#             for i in range(1, 1000000):
#                 self.assertEqual(i, d.get(str(i)))


#     def test_py_dict(self):

#         d = dict()
#         for i in range(1, 1000000):
#             d[str(i)] = i

#         for i in range(1, 1000000):
#             d.get(i)
